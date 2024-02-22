from django.contrib import admin
from .models import (
    Author,
    Tag,
    Blog,
    Comment,
    BlogContent
)


class BlogContentAdmin(admin.TabularInline):
    model = BlogContent
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('blog',)
    list_display_links = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('blog',)
    list_display_links = ('title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogContentAdmin]
    list_display = ('id', 'title', 'created_date',)
    search_fields = ('author', 'title',)
    list_display_links = ('title',)
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)
    readonly_fields = ('created_date', 'slug',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'created_date',)
    search_fields = ('blog', 'author',)
    list_display_links = ('message',)
    date_hierarchy = 'created_date'

