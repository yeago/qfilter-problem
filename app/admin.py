from django.contrib import admin

from app import models


class InfoAdmin(admin.ModelAdmin):
    list_filter = ['contact__date', 'contact__person']

admin.site.register(models.Info, InfoAdmin)


admin.site.register(models.Person)
admin.site.register(models.Contact)
