from django import template
from django.core.urlresolvers import resolve
from accounts.models import Profile, Company

register = template.Library()

@register.inclusion_tag('_navigation.html', takes_context=True)
def get_navigation(context):
    request = context.get('request')
    user = request.user 
    profile = ''
    company = ''

    if request.user.is_authenticated():
        profile = Profile.objects.get(user=user)

        # Company account
        if profile.account_type == 2:    
            company = Company.objects.get(id=profile.company_id)            

    return {
        'user': user,
        'profile': profile,
        'company': company
    }