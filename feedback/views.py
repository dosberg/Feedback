from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.conf import settings
from django.contrib import messages
from forms import FeedbackForm, QuestionForm
from feedback.models import Request, Question


def feedback_request(request):
    user = request.user

    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    QuestionFormSet = formset_factory(QuestionForm, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST': 

        request_user = Request(user=request.user)
        request_form = FeedbackForm(request.POST, instance=request_user) # A form bound to the POST data
      
        # Create a formset from the submitted data
        question_formset = QuestionFormSet(request.POST, request.FILES)

        if request_form.is_valid() and question_formset.is_valid():
            request = request_form.save()
          
            for form in question_formset.forms:

                question = form.save(commit=False)
                question.request = request
                question.save()
              
            ''' 

            TODO: make this work 
            messages.success(request, 'Your request for feedback was sent to {{ email address }}!')
           
            '''
            return redirect('dashboard')
    else:
        request_form = FeedbackForm()
        question_formset = QuestionFormSet()

    return render_to_response('request.html', {
        'request_form': request_form,
        'question_formset': question_formset,
        'user': user,
    }, RequestContext(request))


@login_required
def feedback_questions(request, url):
    user = request.user
    feedback_detail = Request.objects.filter(url=url)


    # TODO: cleanup this mess and make work
    if request.method == 'POST': 

        for request in feedback_detail:
            request_id = request.id

            feedback_questions = Question.objects.filter()
    else:        

        for request in feedback_detail:
            request_id = request.id

            feedback_questions = Question.objects.filter()

    return render_to_response('questions.html', {
        'feedback_detail': feedback_detail,
        'feedback_questions': feedback_questions,
        'user': user,
    }, RequestContext(request))
