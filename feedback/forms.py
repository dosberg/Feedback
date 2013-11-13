from django import forms

class FeedbackForm(forms.Form):
    to = forms.CharField(max_length=255)
    cc   = forms.CharField(max_length=255)