from django.contrib import admin

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'author', 'tags')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title', 'content', 'author')
    list_per_page = 10

admin.site.register(BlogPost, BlogPostAdmin)
