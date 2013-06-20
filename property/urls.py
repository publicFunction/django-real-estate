from django.conf.urls import patterns, include, url

urlpatterns = patterns('property.views',
    url(r'^$', 'index' , name='homepage'),
    url(r'^property/(?P<id>\d+)/$', 'property', name='view_property'),
    url(r'^residential/$', 'residential', name='residentail'),
    url(r'^commercial/$', 'commercial', name='commercial')
)