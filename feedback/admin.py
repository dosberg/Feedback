from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from feedback.models import Request, Question

class QuestionsAdmin(admin.ModelAdmin):

    list_display = ('question',)

admin.site.register(Question, QuestionsAdmin)


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('to', 'invite', 'timestamp')

admin.site.register(Request, FeedbackAdmin)