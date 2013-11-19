#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from feedback.views import Request, Question
from userena.utils import signin_redirect, get_profile_model, get_user_model
from django.contrib import messages

def index(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    else:    

	return render_to_response('index.html', {}, context_instance=RequestContext(request))


@login_required
def dashboard(request):
	feedback_questions = []
	user = request.user 
	profile = user.get_profile() 

	feedback_requests = Request.objects.filter(user=user).order_by('timestamp').reverse()

	for request in feedback_requests:
		request_id = request.id
		feedback_questions = Question.objects.filter()

	return render_to_response('dashboard.html', {
		'feedback_requests': feedback_requests,
		'feedback_questions': feedback_questions,
		'profile': profile,
		}, context_instance=RequestContext(request))


@login_required
def company_dashboard(request):
	feedback_questions = []
	user = request.user
	profile = user.get_profile()

	# Only allow user who have a Company and are Admins
	if profile.account_type == 2 and profile.role == 2:
		feedback_requests = Request.objects.filter(user=user).order_by('timestamp').reverse()

		for request in feedback_requests:
			request_id = request.id
			feedback_questions = Question.objects.filter()

		return render_to_response('company_dashboard.html', {
			'feedback_requests': feedback_requests,
			'feedback_questions': feedback_questions,
			'profile': profile,
			}, context_instance=RequestContext(request))		
	else: 
		return redirect('/dashboard/')			


def plans(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    else:    

	return render_to_response('plans.html', {}, context_instance=RequestContext(request))