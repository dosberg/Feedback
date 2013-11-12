"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^$', direct_to_template,
            { 'template': 'index.html' }, 'index'),
)