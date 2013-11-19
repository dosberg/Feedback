from django.conf import settings
from django.conf.urls import patterns, url
from www.views import index, dashboard, plans

urlpatterns = patterns('',

    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^plans/$', plans, name='plans'),
    url(r'', index, name='index'),
)