from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from quotes.models import Quote
from utils.views import paginate

def list(request):
    quotes = Quote.objects.all().order_by('-id')
    return render(request, 'quotes/list.html', {'quotes': paginate(request, quotes)})

def nick(request, nick):
    by_nick = Quote.objects.filter(nick__icontains=nick).order_by('-id')[:5]
    about_nick = Quote.objects.filter(quote__icontains=nick).order_by('-id')[:5]
    return render(request, 'quotes/nick.html', {'by_nick': by_nick, 'about_nick': about_nick, 'nick': nick})

def search(request):
    query = request.REQUEST.get('q', None)
    if query is not None:
        results = Quote.objects.filter(quote__icontains=query).order_by('-id')
        return render(request, 'quotes/search.html', {'results': paginate(request, results), 'query': query})
    else:
        raise Http404

def quote(request, quote_id):
    q = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/quote.html', {'quote': q})

def vote(request, quote_id):
    q = get_object_or_404(Quote, pk=quote_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['vote'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'quotes/quote.html', {
            'quote': q,
            'error_message': "You didn't select a quote.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('quotes.views.quote', args=(q.id,)))
