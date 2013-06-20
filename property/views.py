from django.shortcuts import render_to_response
from django.template.context import RequestContext
from property.models import Property, FeaturedProperty, PropertyChoice

def index(request):
	featured = Property.objects.filter(featured=1).order_by('?')[:2]
	return render_to_response(  'home/index.html',
								{
									'featured': featured,
								},
								context_instance=RequestContext(request)
							)

def residential(request):
	prop_choice = PropertyChoice.objects.get(value='res')
	property = Property.objects.filter(property_type=prop_choice).order_by('reference')
	return render_to_response(  'property/property_list.html',
								{
									'properties' : property,
									'page_title' : prop_choice
									
								},
								context_instance=RequestContext(request)
							)
	

def commercial(request):
	prop_choice = PropertyChoice.objects.get(value='comm')
	property = Property.objects.filter(property_type=prop_choice).order_by('reference')
	return render_to_response(  'property/property_list.html',
								{
									'properties' : property,
									'page_title' : prop_choice
								},
								context_instance=RequestContext(request)
							)

def property(request, id):
	pass