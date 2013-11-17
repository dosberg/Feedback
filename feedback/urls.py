from django.conf.urls import *
 
import views
 
urlpatterns = patterns('', 
 
    #url(r'^''$', views.feedback_list, name='feedback_list'),  
    url(r'^request/$', views.feedback_request, name='feedback_request'),   
    url(r'^(?P<url>\w+)$', views.feedback_questions, name="feedback_questions"),    
    url(r'', views.feedback_questions, name="feedback")
)