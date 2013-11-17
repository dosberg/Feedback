from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from feedback.models import Request, Question

class QuestionsAdmin(admin.ModelAdmin):

    list_display = ('question',)

admin.site.register(Question, QuestionsAdmin)


class FeedbackAdmin(admin.ModelAdmin):

	# def questions(self):
	# 	return self.question.get_questions_display()

	list_display = ('id', 'email', 'invite', 'timestamp',)

admin.site.register(Request, FeedbackAdmin)