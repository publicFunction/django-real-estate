from django.contrib import admin

from models import *

class SiteTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'active',)

admin.site.register(SiteTitle, SiteTitleAdmin)

class SiteHeaderImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'image', 'active',)
    
admin.site.register(SiteHeaderImage, SiteHeaderImageAdmin)
