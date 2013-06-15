import string, collections
from django import template
from django.template.context import RequestContext
from django.http import HttpRequest

from banner.models import Banner, BannerImages

register = template.Library()

@register.inclusion_tag('home/slider.html', takes_context=True)
def homepage_slider(context):
	images = BannerImages.objects.filter(banner__name="Homepage Banner")
	return {'banner' : images}