import realestate

from site_setup.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def global_data(request):
	global_site_title = SiteTitle.objects.get(active=1)
	default_header_image = SiteHeaderImage.objects.get(active=1)

	global_data = {	'site_title': global_site_title.title,
					'title_sep' : global_site_title.seperator,
					'header_image' : default_header_image.image,
					'header_image_alt' : default_header_image.alt,
				}

	return global_data

