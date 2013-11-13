from django.contrib import admin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from feedback.models import Request, Question


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('user', 'to', 'cc', 'timestamp')

admin.site.register(Request, FeedbackAdmin)
