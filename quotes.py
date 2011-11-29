import os, datetime
from chii import command
from collections import Counter
import re

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from quotes.models import Quote

@command('+q', 'q+', 'addquote')
def add_quote(self, channel, nick, host, *args):
    """adds quote to database"""
    q = Quote(nick=nick, host=host, channel=channel, added=datetime.datetime.now(), quote=' '.join(args))
    q.save()
    return 'added quote %d' % q.id

@command('-q', 'q-', 'rmquote')
def del_quote(self, channel, nick, host, *args):
    """deletes quote from database"""
    try:
        id = int(args[0])
        q = Quote.objects.get(id=id)
    except:
        return 'eh? what quote?'

    if q.host == host:
        q.delete()
        return 'deleted quote %d' % id
    else:
        return 'not your quote bub'

@command('q', 'quote')
def quote(self, channel, nick, host, *args):
    """gets quotes from database random, by id, or search"""
    def rand():
        q = Quote.objects.order_by('?')
        if q:
            return '[%d] %s' % (q[0].id, q[0].quote.encode('ascii', errors='replace'))
        else:
            return 'quote not found'

    def get_id(q_id):
        q = Quote.objects.get_or_none(id=q_id)
        if q:
            return '[%d] %s' % (q.id, q.quote.encode('ascii', errors='replace'))
        else:
            return 'quote not found'

    def search(query):
        q = Quote.objects.filter(quote__icontains=query).order_by('?')
        if q:
            return '[%d] %s' % (q[0].id, q[0].quote.encode('ascii', errors='replace'))
        else:
            return 'quote not found'

    if args:
        try:
            return get_id(int(args[0]))
        except:
            return search(' '.join(args))
    else:
        return rand()

@command('lastquote', 'lq', 'ql')
def last_quote(self, channel, nick, host, *args):
    q = Quote.objects.order_by('-id')[0]
    return '[%s] %s' % (q.id, str(q.quote))

@command('mostquotes', 'q10', 'top10')
def top_10(self, channel, nick, host, *args):
    all = [q.quote.lower() for q in Quote.objects.all()]
    quotes = [[x for x in re.findall(r'[<\[][@+]?([\w|_`]+)[>\]]', q) if x] for q in all]
    actions = [[x for x in re.findall(r'\*\s([\w|`]+)', q) if x] for q in all]
    cnt = Counter(sum([list(set(x)) for x in quotes+actions], []))
    return '\002top 10 most quoted\002: ' + ', '.join(': '.join([nick, str(count)]) for nick, count in cnt.most_common()[:10])
