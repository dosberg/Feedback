import os
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from binascii import hexlify

def createHash():
	return hexlify(os.urandom(10))

class Request(models.Model):
    user = models.ForeignKey(User) #user_id in db
    name = models.CharField(max_length=255)
    email   = models.EmailField(blank=False, max_length=75)
    invite   = models.CharField(blank=True, max_length=255)
    viewed = models.BooleanField(default=False)
    viewed_timestamp = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=20,default=createHash,unique=True)

class Question(models.Model):
	user_id = models.CharField(User, max_length=255)
	question   = models.TextField(blank=True, max_length=644)
	request = models.ForeignKey(Request) #request_id in db

	@staticmethod
	def get_questions(user):
		return Question.objects.filter()

class Answer(models.Model):
	user_id = models.CharField(User, max_length=255)
	answer = models.TextField(blank=True, max_length=644)
	question   = models.ForeignKey(Question) #question_id in db