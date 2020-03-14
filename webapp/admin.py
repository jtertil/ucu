from django.contrib import admin
from django.contrib.auth.models import Group

from .models import ShortCut


class ShortCutAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pk_encode', 'url')


admin.site.site_header = "UCU administration site"
admin.site.register(ShortCut, ShortCutAdmin)
admin.site.unregister(Group)
