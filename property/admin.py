from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from models import *

class PropertyAdminForm(forms.ModelForm):
	property_desc = forms.CharField(widget=CKEditorWidget())
	location_desc = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Property

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm

admin.site.register(Property, PropertyAdmin)

class CountryAdmin(admin.ModelAdmin):
	exclude = ('slug','short_code',)

admin.site.register(Country, CountryAdmin)