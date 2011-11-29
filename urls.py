from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^quotes/', include('quotes.urls')),
    url(r'^$', 'quotes.views.list', name='home'),
)
