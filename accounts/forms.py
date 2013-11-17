from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupFormOnlyEmail

class SignupFormExtra(SignupFormOnlyEmail):

    account_type_choices = (
        ('', "-- Select --"),
        (1, "Individual"),
        (2, "Company"),
    )
    account_type = forms.ChoiceField(label=_("Account type:"), 
        choices=account_type_choices, required=True)

    first_name = forms.CharField(label=_(u'First name'),
        max_length=30,
        required=True)

    last_name = forms.CharField(label=_(u'Last name'),
        max_length=30,
        required=True)

    def __init__(self, *args, **kw):

        super(SignupFormExtra, self).__init__(*args, **kw)

        new_order = self.fields.keyOrder[:-3]
        new_order.insert(0, 'account_type')
        new_order.insert(1, 'first_name')
        new_order.insert(2, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):

        new_user = super(SignupFormExtra, self).save()

        new_user.account_type = self.cleaned_data['account_type']
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()

        return new_user
