from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index1, name='index1'),
    path('catalog/', views.index2, name='index2'),
    path('add_game/', views.index3, name='index3'),
    path('sign-in/', views.index4, name='index4'),
    path('register/', views.index5, name='index5'),
]