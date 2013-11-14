from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import FeedbackForm

from feedback.models import Request, Question

@login_required
def feedback_request(request):
    if request.method == 'POST':
        
        form = FeedbackForm(request.POST)
        if form.is_valid(): 
            
            pass
            # send back to feedback dashboard
    else:
        form = FeedbackForm() 

    return render_to_response('request.html', {
        'form': form,
    }, RequestContext(request))

@login_required
def feedback_list(request):
    user = request.user

    queryset = Request.objects.all()

    feedback = queryset.query

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