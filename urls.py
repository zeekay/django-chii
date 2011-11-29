from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^links/', include('links.urls')),
    (r'^quotes/', include('quotes.urls')),
    (r'^$', include('core.urls')),
)
