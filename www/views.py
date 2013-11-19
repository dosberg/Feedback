#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from feedback.views import Request, Question
from django.contrib import messages

def index(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    else:    

	return render_to_response('index.html', {}, context_instance=RequestContext(request))


def dashboard(request):
	feedback_questions = []
	user = request.user

	feedback_requests = Request.objects.filter(user=user).order_by('timestamp').reverse()

	for request in feedback_requests:
		request_id = request.id

		feedback_questions = Question.objects.filter()

	return render_to_response('dashboard.html', {
		'feedback_requests': feedback_requests,
		'feedback_questions': feedback_questions,
		}, context_instance=RequestContext(request))	


def plans(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
    else:    

	return render_to_response('plans.html', {}, context_instance=RequestContext(request))