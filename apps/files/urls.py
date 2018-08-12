# -*- coding: utf-8 -*-
from django.urls import path

from . import views as files_views

urlpatterns = [
    path('', files_views.index),
    path('login/', files_views.login),
    path('logout/', files_views.logout),
    path('special/lists/', files_views.special_lists),
    path('special/lists/<ctg>/', files_views.special_labels),
    path('special/lists/<ctg>/detail', files_views.show_special_detail),
]
