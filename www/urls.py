from django.conf import settings
from django.conf.urls import patterns, url
from www.views import index, dashboard, company_dashboard, plans

urlpatterns = patterns('',

    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^company/dashboard/$', company_dashboard, name='company_dashboard'),
    url(r'^plans/$', plans, name='plans'),
    url(r'', index, name='index'),
)