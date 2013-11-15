#from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from feedback.views import Request, Question
from django.contrib import messages

def index(request):
	
	return render_to_response('index.html', {}, context_instance=RequestContext(request))


def dashboard(request):
	user = request.user
	feedback_questions = []

	feedback_requests = Request.objects.filter(user=request.user).order_by('timestamp').reverse()

	for request in feedback_requests:
		request_id = request.id

		feedback_questions = Question.objects.filter()

		# for question in feedback_questions:
		# 	print question.request_id


	return render_to_response('dashboard.html', {
		'feedback_requests': feedback_requests,
		'feedback_questions': feedback_questions,
		}, context_instance=RequestContext(request))	
