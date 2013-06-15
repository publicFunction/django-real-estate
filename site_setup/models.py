from django.db import models

class SiteTitle(models.Model):
    title = models.CharField(max_length=300)
    seperator = models.CharField(max_length=2)
    active = models.BooleanField(default=0)
    
    def save(self):
        if self.pk is not None:
            if self.active == 1:
                for title in SiteTitle.objects.filter(active=1):
                    title.active = 0
                    title.save()
        super(SiteTitle, self).save()
        
    
    def __unicode__(self):
        return self.title 
     
    class Meta:
        verbose_name="Global Site Title"
        verbose_name_plural="Global Site Title"

class SiteHeaderImage(models.Model):
    alt = models.CharField(max_length=300)
    image = models.ImageField(upload_to="global/images/")
    active = models.BooleanField(default=0)
    
    def save(self):
        if self.pk is not None:
            if self.active == 1:
                for header in SiteHeaderImage.objects.filter(active=1):
                    header.active = 0
                    header.save()
        super(SiteHeaderImage, self).save()
    
    def __unicode__(self):
        return self.alt
    
    class Meta:
        verbose_name="Global Site Header Image"
        verbose_name_plural="Global Site Header Image"

class SiteCurrencyList(models.Model):
    currency_symbol = models.CharField(max_length=10)
    currency_code = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.currency_symbol
    
    class Meta:
        verbose_name="Global Site Currency List"
        verbose_name_plural="Global Site Currency List"

class SiteCurrency(models.Model):
    currency = models.ForeignKey('SiteCurrencyList')
    
    def __unicode__(self):
        return self.currency
    
    class Meta:
        verbose_name="Global Site Set Currency"
        verbose_name_plural="Global Site Set Currency"
    
    