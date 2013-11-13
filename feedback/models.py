from django.db import models
from django.contrib.auth.models import User
 
class Request(models.Model):

    user = models.ForeignKey(User,)
    to   = models.CharField(max_length=255)
    cc   = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class Question(models.Model):

    user = models.ForeignKey(User,)
    question   = models.CharField(max_length=255)
    request_id = models.IntegerField(null=True, blank=False)
