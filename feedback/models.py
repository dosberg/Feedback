from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
 
class Request(models.Model):

    user = models.ForeignKey(User)
    to   = models.CharField(max_length=255)
    invite   = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

def __unicode__(self):
    return unicode(self.id)




class Question(models.Model):

    user = models.OneToOneField(User)
    question   = models.CharField(max_length=255)
    request = models.ForeignKey(Request)

def __unicode__(self):
    return unicode(self.user)




# class TodoList(models.Model):
#     name = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.name


# class TodoItem(models.Model):
#     name = models.CharField(max_length=150,
#                help_text="e.g. Buy milk, wash dog etc")
#     list = models.ForeignKey(TodoList)

#     def __unicode__(self):
#         return self.name + " (" + str(self.list) + ")"
