from django.contrib import admin

from .models import Post


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
