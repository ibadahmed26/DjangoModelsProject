from django.contrib import admin
from .models import *


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'date']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'date']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'date','duration','get_singers']
