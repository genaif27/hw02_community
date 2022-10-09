# posts/urls.py
from urllib import request
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='posts'),
    path('group/<slug>/', views.group_list, name='group_list'),
]