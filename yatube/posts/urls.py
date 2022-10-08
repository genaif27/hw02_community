# posts/urls.py
from urllib import request
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.index, name='index'),
    path('posts/', views.group_list, name='group_list'),
]