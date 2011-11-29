from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'index',   name='home'),
)
