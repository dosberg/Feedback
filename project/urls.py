from django.conf.urls import patterns, include, url
from www import urls as www_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('userena.urls')),
    url('', include(www_urls)),
)