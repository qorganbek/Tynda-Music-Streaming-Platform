from django.contrib import admin
from . import models


class AdminAudio(admin.ModelAdmin):
    list_display = ['artist', 'id', 'artist', 'title', 'is_top']
    list_filter = ['title', 'artist']
    search_fields = ['title', 'artist']
    list_editable = ['is_top']
    list_per_page = 50


admin.site.register(models.Audio, AdminAudio)
