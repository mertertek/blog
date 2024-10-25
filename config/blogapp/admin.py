from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['user','title', 'created_at','status']


admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user', 'created_at']

admin.site.register(Comment, CommentAdmin)