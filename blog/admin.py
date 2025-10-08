from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'author',
                    'created',
                    'publish',
                    'updated',
                    'status',
                    ]
    list_filter = ['status', 'title']
    search_fields = ['title']
    ordering = ['status']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']