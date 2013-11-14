from django.conf import settings
from django.conf.urls import patterns, url
from www.views import index, dashboard

urlpatterns = patterns('',

    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'', index, name='index'),
)