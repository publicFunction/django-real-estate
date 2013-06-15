from django.conf.urls import patterns, include, url

urlpatterns = patterns('property.views',
    url(r'^$', 'index' , name='homepage'),

)