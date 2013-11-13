from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from forms import FeedbackForm

from models import Feedback


def feedback_request(request):
    if request.method == 'POST':
        
        form = FeedbackForm(request.POST)
        if form.is_valid(): 
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = FeedbackForm() 

    return render(request, 'request.html', {
        'form': form,
    })


def feedback_list(request):
    user = request.user
    feedback_list = User.objects.all()
    feedback_list = Feedback.objects.filter(user__pk=user.pk)

    return render_to_response('list.html', {
        'feedback_list': feedback_list,
        'user': user,
    }, RequestContext(request))




def feedback_detail(request, id):
    user = request.user
    feedback_detail = Feedback.objects(id)

    return render_to_response('detail.html', {
        'feedback_detail ': feedback_detail ,
        'user': user,
    }, RequestContext(request))

 
           
 


def feedback_update(request, id):
 
    return update_object(request,
        model=Feedback,
        object_id=id,
        template_name='feedback/update.html',
        post_save_redirect=reverse("feedback_list")
    )            
 
def feedback_delete(request, id):
 
    return delete_object(request,
        model=Feedback,
        object_id=id,
        template_name='feedback/delete.html',
        post_delete_redirect=reverse("feedback_list")
    )