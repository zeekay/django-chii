from django.conf.urls.defaults import *

urlpatterns = patterns('links.views',
    url(r'^$',                   'list',   name='links-list'),
    url(r'^search/$',            'search', name='links-search'),
    url(r'^nick/(\w+)/$',        'nick',   name='links-nick'),
    url(r'^link/(\d+)/$',        'link',  name='links-link'),
    url(r'^(\d+)/vote/(\d{1})$', 'vote',   name='links-vote'),
)
