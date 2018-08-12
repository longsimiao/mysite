# -*- coding: utf-8 -*-

from django.urls import path

from . import views as blog_views


urlpatterns = [
    path('lists/', blog_views.lists),
    path('lists/<ctg>/', blog_views.category),
    path(r'lists/<ctg>/detail/', blog_views.detail),
]

