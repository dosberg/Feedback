from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from accounts.models import Company

class CompanyAdmin(admin.ModelAdmin):

	list_display = ('id', 'name', 'creator_id', 'date_created',)

admin.site.register(Company, CompanyAdmin)