from django.conf import settings
from django.conf.urls import patterns, url
from www.views import index

urlpatterns = patterns('',

    url(r'', index, name='index'),
)