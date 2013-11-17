from django.forms import ModelForm
from feedback.models import Request, Question

class FeedbackForm(ModelForm):
	class Meta:
		model = Request
		exclude = ('user','viewed', 'viewed_timestamp', 'url',)
    

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ('question',)

	def __init__(self, *args, **kwargs):
	    super(QuestionForm, self).__init__(*args, **kwargs)
	    self.fields['question'].label = "Ask a question (e.g. What am I doing well?)"


	# def save(self,user, commit=True, *args, **kwargs):
	# 	question = super(QuestionForm, self).save(commit=False,*args, **kwargs)
	# 	question.owner = user
	# 	if commit:
	# 		question.save()
	# 	return question