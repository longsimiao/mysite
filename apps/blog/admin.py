from django.contrib import admin
from apps.blog.models import Category, Label, Blog, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id', 'edit_time')
    ordering = ('-edit_time', 'description')


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('label', 'id', 'edit_time')
    ordering = ('-edit_time',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'id', 'edit_time')
    ordering = ('-edit_time',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_active', 'edit_time')
    ordering = ('-edit_time',)
    search_fields = ['title', 'body', ]
    list_per_page = 10


