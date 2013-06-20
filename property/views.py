from django.shortcuts import render_to_response
from django.template.context import RequestContext
from property.models import Property, FeaturedProperty

def index(request):
	featured = Property.objects.filter(featured=1).order_by('?')[:2]
	return render_to_response(  'home/index.html',
								{
									'featured': featured,
								},
								context_instance=RequestContext(request)
							)

def residential(request):
	return render_to_response(  'property/property_list.html',
								{
									
								},
								context_instance=RequestContext(request)
							)
	

def commercial(request):
	return render_to_response(  'property/property_list.html',
								{
									
								},
								context_instance=RequestContext(request)
							)