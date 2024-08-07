from django.contrib import admin
from comments.models import *

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'created_by', 'publication', 'created_at', 'updated_at')
    search_fields = ('comment_text', 'created_by__username', 'publication__title')
    list_filter = ('created_at', 'updated_at', 'created_by', 'publication')

