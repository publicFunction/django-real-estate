from django.contrib import admin
from django.db import models

from realestate import settings
from models import Banner, BannerImages

class BannerImagesInline(admin.StackedInline):
    model = BannerImages
    
    
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImagesInline,]
    
    
admin.site.register(Banner, BannerAdmin)