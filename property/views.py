from django.shortcuts import render_to_response
from django.template.context import RequestContext
from property.models import Property, FeaturedProperty

def index(request):
	featuredList = []
	for fp in FeaturedProperty.objects.all().order_by('?')[:2]:
		fp = Property.objects.get(pk=fp.property_id)
		featuredList.append(fp)
	featured = {'featured' : featuredList}
	
	return render_to_response(  'home/index.html',
								{
									'featured': featured,
								},
								context_instance=RequestContext(request)
							)
