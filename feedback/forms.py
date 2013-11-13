from django import forms

class FeedbackForm(forms.Form):
    title   = forms.CharField(max_length=255)
    content = forms.CharField()