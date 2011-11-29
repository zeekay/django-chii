from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from utils.views import paginate
from links.models import Link

def list(request):
    links = Link.objects.all().order_by('-id')
    return render(request, 'links/list.html', {'links': paginate(request, links, per_page=50)})

def nick(request, nick):
    by_nick = Link.objects.filter(nick__icontains=nick).order_by('-id')[:50]
    about_nick = Link.objects.filter(link__icontains=nick).order_by('-id')[:50]
    return render(request, 'links/nick.html', {'by_nick': by_nick, 'about_nick': about_nick, 'nick': nick})

def search(request):
    query = request.REQUEST.get('q', None)
    if query is not None:
        results = Link.objects.filter(link__icontains=query).order_by('-id')
        return render(request, 'links/search.html', {'results': paginate(request, results), 'query': query})
    else:
        raise Http404

def link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'links/link.html', {'link': link})

def vote(request, link_id):
    q = get_object_or_404(Link, pk=link_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['vote'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'links/link.html', {
            'link': link,
            'error_message': "You didn't select a link.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('links.views.link', args=(link.id,)))
