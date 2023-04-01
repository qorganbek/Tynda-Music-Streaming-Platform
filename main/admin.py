from django.contrib import admin
from . import models


class AdminSong(admin.ModelAdmin):
    list_display = ['title', 'id', 'is_top', 'category']
    list_editable = ['is_top']
    search_fields = ['title', 'id']


admin.site.register(models.Song, AdminSong)
admin.site.register(models.Category)
admin.site.register(models.Artist)
