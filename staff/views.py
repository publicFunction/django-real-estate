from django.shortcuts import render_to_response
from django.template.context import RequestContext
from staff.models import Staff

def staff(request):
    owners = Staff.objects.all().filter(position__exact='OW')
    staffList = Staff.objects.all().filter(position__exact='EM')
    return render_to_response(  'home/about.htm', 
                                {'owners' : owners,
                                 'stafflist':staffList}, 
                                context_instance=RequestContext(request))