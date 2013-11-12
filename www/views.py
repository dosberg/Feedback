#from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

def index(request):
	
	return render_to_response('index.html', {}, context_instance=RequestContext(request))