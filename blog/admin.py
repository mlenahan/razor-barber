from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Reply


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """ Admin view for Blog Posts """
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('title', 'created')
    summernote_fields = ('body')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """Admin view for Replies"""
    list_display = ('post', 'created', 'creator')
    search_fields = ('body', 'creator__username')
    list_filter = ('creator__username', 'created')
