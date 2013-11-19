from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')

class Company(models.Model):
	name   = models.TextField(blank=True, max_length=644) 
	date_created = models.DateTimeField(auto_now_add=True) 
	creator_id = models.CharField(User, max_length=255)	