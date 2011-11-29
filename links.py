import argparse, datetime, os, re, shlex
import lxml.html

from chii import command, event

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models import Q
from links.models import Link

# regex for finding links
regex = re.compile(r'https?://\S+\.\S+')

# parser for determing search queries
parser = argparse.ArgumentParser()
parser.add_argument('query', action="store", nargs='?')
parser.add_argument('-user', action='store')
parser.add_argument('-title', action='store')
parser.add_argument('-context', action='store')
parser.add_argument('-all', action='store')

def url_processing(url):
    """process some links for cleaner database"""
    if 'youtube.com/' in url:
        url = url.split('&')[0]
    return url

def title_processing(title):
    """process titles for nicer titles"""
    return ' '.join(x.strip() for x in title.strip().encode('ascii', errors='ignore').splitlines()) # srsly youtube?

@event('msg')
def add_link(self, channel, nick, host, msg):
    """adds link to database"""
    if not host.startswith('~muse'):
        urls = regex.findall(msg)
        if urls:
            for url in [u for u in urls if 'notune' not in u]:
                url = url_processing(url)
                try:
                    tree = lxml.html.parse(url)
                    title = title_processing(tree.xpath('//title/text()')[0])
                    self.msg(channel, title)
                except:
                    title = ''
                link = Link(nick=nick,
                            host=host,
                            channel=channel,
                            added=datetime.datetime.now(),
                            link=url,
                            context=msg,
                            title=title)
                try: link.save()
                except: pass

@command('l', 'link', 'links')
def search_links(self, channel, nick, host, *args):
    """retrieves links from database random, by id, or search"""

    def rand():
        """returns random links"""
        links = Link.objects.order_by('?')[:1]
        if links:
            link = links[0]
            msg = '[%d] %s' % (link.id, str(link.link))
            if link.title:
                msg += ' - %s' % str(link.title)
            return msg
        return 'link not found'

    def get_id(link_id):
        """returns link by id"""
        link = Link.objects.get_or_none(id=link_id)
        if link:
            msg = '[%d] %s' % (link.id, str(link.link))
            if link.title:
                msg += ' - %s' % str(link.title)
            return msg
        return 'link not found'

    def search(args):
        """handles searches for links"""
        q_objs = {
            'query': lambda x: Q(link__icontains=x),
            'context': lambda x: Q(context__icontains=x),
            'title': lambda x: Q(title__icontains=x),
            'user': lambda x: Q(nick__icontains=x),
        }

        def and_q_objs(query):
            """returns AND'd together Q objects"""
            return Link.objects.filter(reduce(lambda x,y: x | y, [x(query) for x in q_objs.values()])).distinct()

        def or_q_objs(queries):
            """returns OR'd together Q objects"""
            return Link.objects.filter(reduce(lambda x,y: x & y, [q_objs[k](v) for k,v in queries if v])).distinct()

        try: args = parser.parse_args(shlex.split(' '.join(args)))
        except: return 'invalid search'

        links = and_q_objs(args.all) if args.all else or_q_objs(args._get_kwargs())
        if links:
            for link in links[:5]:
                msg = '[%d] %s' % (link.id, str(link.link))
                if link.title:
                    msg += ' - %s' % str(link.title)
                self.batch_msg(channel, msg)
            return '%d links found' % len(links)
        return 'link not found'

    if args:
        try: return get_id(int(args[0]))
        except: return search(args)
    return rand()

@command('lastlink', 'll')
def last_link(self, channel, nick, host, *args):
    link = Link.objects.order_by('-id')[0]
    return '[%s] %s' % (link.id, str(link.link))
