from django.shortcuts import render_to_response
from django.template.context import RequestContext
from contactus.models import ContactUsForm
from django.forms.models import modelformset_factory

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('home/thanks.htm',{}, context_instance=RequestContext(request))
    else:
        form = ContactUsForm()
    return render_to_response('home/contact.htm',
                              { 'contactform' : form},
                              context_instance=RequestContext(request))