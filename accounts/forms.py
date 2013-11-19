from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupFormOnlyEmail
from userena.models import UserenaBaseProfile
from accounts.models import Company

class SignupFormExtra(SignupFormOnlyEmail):

    first_name = forms.CharField(label=_(u'First name'),
        max_length=30,
        required=True)

    last_name = forms.CharField(label=_(u'Last name'),
        max_length=30,
        required=True)

    def __init__(self, *args, **kw):

        super(SignupFormExtra, self).__init__(*args, **kw)

        new_order = self.fields.keyOrder[:-2]
        new_order.insert(0, 'first_name')
        new_order.insert(1, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):

        user = super(SignupFormExtra, self).save()

        user_profile = user.get_profile()
        user_profile.account_type = '1'
        user_profile.save()

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user



class CompanySignupFormExtra(SignupFormOnlyEmail):

    company_name = forms.CharField(label=_(u'Company name'),
        max_length=30,
        required=True)

    first_name = forms.CharField(label=_(u'First name'),
        max_length=30,
        required=True)

    last_name = forms.CharField(label=_(u'Last name'),
        max_length=30,
        required=True)

    def __init__(self, *args, **kw):

        super(CompanySignupFormExtra, self).__init__(*args, **kw)

        new_order = self.fields.keyOrder[:-3]
        new_order.insert(0, 'company_name')
        new_order.insert(1, 'first_name')
        new_order.insert(2, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):

        user = super(CompanySignupFormExtra, self).save()

        company_name = self.cleaned_data['company_name']
        creator_id = user.id
        company = Company.objects.create(name=company_name, creator_id=creator_id)

        user_profile = user.get_profile()
        user_profile.account_type = '2'
        user_profile.role = '2'
        user_profile.save()

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user