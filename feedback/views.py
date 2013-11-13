from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from feedback.forms import FeedbackForm

from feedback.models import Request, Question


def feedback_request(request):
    if request.method == 'POST':
        
        form = FeedbackForm(request.POST)
        if form.is_valid(): 
            
            pass
            # send back to feedback dashboard
    else:
        form = FeedbackForm() 

    return render(request, 'request.html', {
        'form': form,
    })


def feedback_list(request):
    user = request.user
    feedback = Request.objects.filter()

    return render_to_response('list.html', {
        'feedback': feedback,
        'user': user,
    }, RequestContext(request))


def feedback_detail(request, id):
    user = request.user
    feedback_detail = Feedback.objects(id)

    return render_to_response('detail.html', {
        'feedback_detail ': feedback_detail ,
        'user': user,
    }, RequestContext(request))