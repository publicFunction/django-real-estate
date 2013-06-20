from django.db import models

from property.models import City

class Office(models.Model):
    name = models.CharField(max_length=350)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=500)
    city = models.ForeignKey(City)
    postcode = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=500)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        super(Office, self).save(*args, **kwargs)
    
    def get_geo_location(self):
        pass
    
class OfficeGeoLocation(models.Model):
    office = models.ForeignKey('Office')
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __unicode__(self):
        return self.office