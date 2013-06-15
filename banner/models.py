from django.db import models
from django.core.urlresolvers import reverse
from django import forms

class Banner(models.Model):
    LINK_OPTIONS = (('I', 'Image'),
                    ('T', 'Text'),
                    )
    name = models.CharField(max_length=200)
    link_option = models.CharField(max_length=20, choices=LINK_OPTIONS, default="T")
    
    def __unicode__(self):
        return self.name;
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
    
class BannerImages(models.Model):
    banner = models.ForeignKey(Banner);
    image = models.ImageField(upload_to="banner/")
    image_alt = models.CharField(max_length=300)
    link = models.URLField(max_length=500, default="#")
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"
    
    def __unicode__(self):
        return "%s in banner %s" % (self.image_alt, self.banner.name)
