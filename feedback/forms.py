from django.forms import ModelForm
from feedback.models import Request, Question

class FeedbackForm(ModelForm):
	class Meta:
		model = Request
		exclude = ('user',)
    

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ('question', 'user')
		# exclude = ('request','user')

	# def save(self,user, commit=True, *args, **kwargs):
	# 	question = super(QuestionForm, self).save(commit=False,*args, **kwargs)
	# 	question.owner = user
	# 	if commit:
	# 		question.save()
	# 	return question