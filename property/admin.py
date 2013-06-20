from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from models import *

class GardenChoiceAdmin(admin.ModelAdmin):
	pass

admin.site.register(GardenChoice, GardenChoiceAdmin)


class ParkingChoiceAdmin(admin.ModelAdmin):
	pass

admin.site.register(ParkingChoice, ParkingChoiceAdmin)

class SaleStatusAdmin(admin.ModelAdmin):
	pass

admin.site.register(SaleStatus, SaleStatusAdmin)

class PropertyChoiceAdmin(admin.ModelAdmin):
	pass

admin.site.register(PropertyChoice, PropertyChoiceAdmin)

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

class CityAdmin(admin.ModelAdmin):
	pass

admin.site.register(City, CityAdmin)

class ScheduleAdmin(admin.ModelAdmin):
	pass

admin.site.register(Schedule, ScheduleAdmin)

class FloorPlanAdmin(admin.ModelAdmin):
	pass

admin.site.register(FloorPlan, FloorPlanAdmin)

#class FeaturedPropertyAdmin(admin.ModelAdmin):
#	pass
#
#admin.site.register(FeaturedProperty, FeaturedPropertyAdmin)
