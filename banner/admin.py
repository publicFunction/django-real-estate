from django.contrib import admin
from django.db import models
from django import forms

from ckeditor.widgets import CKEditorWidget

from realestate import settings
from models import Banner, BannerImages

class BannerAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BannerImages

class BannerImagesInline(admin.StackedInline):
    model = BannerImages
    form = BannerAdminForm
    
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImagesInline,]
    
    
admin.site.register(Banner, BannerAdmin)