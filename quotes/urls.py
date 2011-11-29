from django.conf.urls.defaults import *

urlpatterns = patterns('quotes.views',
    url(r'^$',                   'list',   name='quotes-list'),
    url(r'^search/$',            'search', name='quotes-search'),
    url(r'^nick/(\w+)/$',        'nick',   name='quotes-nick'),
    url(r'^quote/(\d+)/$',       'quote',  name='quotes-quote'),
    url(r'^(\d+)/vote/(\d{1})$', 'vote',   name='quotes-vote'),
)
