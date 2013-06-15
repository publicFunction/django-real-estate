from django.contrib import admin

from models import *

class PropertyAdmin(admin.ModelAdmin):
	pass


admin.site.register(Property, PropertyAdmin)