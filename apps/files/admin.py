from django.contrib import admin

from .models import PersonalDescription, SpecialArticle
from .models import Label, Author


@admin.register(PersonalDescription)
class PersonalDescriptionForm(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_active', 'edit_time')
    ordering = ('-edit_time',)
    search_fields = ['title', 'type', 'description']
    list_per_page = 10


@admin.register(Label)
class LabelForm(admin.ModelAdmin):
    list_display = ('label', 'edit_time')
    ordering = ('-edit_time', )
    search_fields = ['label', 'description']


@admin.register(Author)
class AuthorForm(admin.ModelAdmin):
    list_display = ('author', 'edit_time')
    ordering = ('-edit_time', )
    search_fields = ['author']


@admin.register(SpecialArticle)
class SpecialArticleForm(admin.ModelAdmin):
    list_display = ('title', 'author', 'label', 'is_active', 'edit_time')
    ordering = ('-edit_time', )
    search_fields = ['title', 'body']
