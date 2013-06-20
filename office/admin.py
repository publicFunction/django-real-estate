from django.contrib import admin

from office.models import Office

class OfficeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Office, OfficeAdmin)