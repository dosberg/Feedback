from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.forms.formsets import formset_factory, BaseFormSet
from django.core.context_processors import csrf
from forms import FeedbackForm, QuestionForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from feedback.models import Request, Question


# def feedback_request(request):
   
#     if request.method == 'POST':
#         newrequest = Request(user=request.user)
#         form = FeedbackForm(request.POST, instance=newrequest)
#         questions = QuestionForm(request.POST)

#         if form.is_valid() and questions.is_valid(): 
           
#            form.save()
#            questions.save()

#            messages.success(request, 'Your request for feedback was sent to {{ email address }}!')
#            return redirect('dashboard')

#     else:
#         form = FeedbackForm() 
#         questions = QuestionForm()

#     return render_to_response('request.html', {
#         'form': form,
#         'questions': questions,
#     }, RequestContext(request))



def feedback_request(request):

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
        question_formset = QuestionFormSet(request.POST)

        if request_form.is_valid() and question_formset.is_valid():
            request = request_form.save()
          
            for form in question_formset.forms:

                question = form.save(commit=False)
                question.request = request
                question.save()
                
                #messages.success(request, 'Your request for feedback was sent to {{ email address }}!')
                return redirect('dashboard')
    else:
        request_form = FeedbackForm()
        question_formset = QuestionFormSet()

    # For CSRF protection
    c = {'request_form': request_form ,
         'question_formset': question_formset,
        }
    c.update(csrf(request))

    return render_to_response('request.html', c)




@login_required
def feedback_list(request):
    user = request.user

    feedback = Request.objects.filter(user=request.user).reverse()

    return render_to_response('list.html', {
        'feedback': feedback,
        'user': user,
    }, RequestContext(request))


@login_required
def feedback_detail(request, id):
    user = request.user
    feedback_detail = Feedback.objects(id)

    return render_to_response('detail.html', {
        'feedback_detail ': feedback_detail ,
        'user': user,
    }, RequestContext(request))