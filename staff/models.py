from django.db import models

class Staff(models.Model):
    OCCUPATION_LIST = (    ('OW','Owner'),
                        ('EM', 'Employee'),
                    )
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=2, choices=OCCUPATION_LIST)
    image = models.FileField(upload_to='staffimages')
    blurb = models.TextField()
    comment = models.TextField(null=True, blank=True, default='')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name="Staff"
        verbose_name_plural="Staff"