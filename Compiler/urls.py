from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('example1', views.example1, name = "home"),
    path('example2', views.example2, name = "home"),
    path('example3', views.example3, name = "home"),
    path('example4', views.example4, name = "home"),
    path('example5', views.example5, name = "home"),
    path('example6', views.example6, name = "home"),
    path('example7', views.example7, name = "home"),
    path('example8', views.example8, name = "home"),
    path('example9', views.example9, name = "home"),
    path('back', views.home, name="home")
]
