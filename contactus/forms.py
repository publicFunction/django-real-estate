from django import forms
from django.forms import Textarea

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        widgets = {
            'message': Textarea(),
        }