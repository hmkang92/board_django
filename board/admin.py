# board/admin.py
from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'detection_at', 'author']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

#admin.site.register(Post)