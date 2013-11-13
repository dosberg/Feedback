from django.contrib import admin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('user', 'title', 'content')

admin.site.register(Feedback, FeedbackAdmin)
