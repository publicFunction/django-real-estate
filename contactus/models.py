from django.db import models
from django import forms
from django.forms import ModelForm, Textarea

class ContactUs(models.Model):
    customer = models.CharField(max_length=300)
    email_address = models.EmailField()
    contact_number = models.CharField(max_length=15)
    message = models.TextField()
    
    def __unicode__(self):
        return "%s at %s contacted us" % (self.customer, self.email_address)
    
    class Meta:
        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        widgets = {
            'message': Textarea(),
        }