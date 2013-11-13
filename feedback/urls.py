from django.conf.urls import *
 
import views
 
urlpatterns = patterns('', 
 
    url(r'^''$', views.feedback_list, name='feedback_list'),  
    url(r'^detail/(?P<id>\d+)/$', views.feedback_detail, name='feedback_detail'),  
    url(r'^request/$', views.feedback_request, name='feedback_request'),   
)