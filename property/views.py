from django.shortcuts import render_to_response
from django.template.context import RequestContext
from property.models import Property, FeaturedProperty
from realestate.settings import MEDIA_URL 

def index(request):
	featuredList = []
	for fp in FeaturedProperty.objects.all().order_by('?')[:2]:
		fp = Property.objects.get(pk=fp.property_id)
		featuredList.append(fp)
	return render_to_response(  'home/index.html',
								{   'featured': featuredList,
									'media_url' : MEDIA_URL
								},
								context_instance=RequestContext(request))
