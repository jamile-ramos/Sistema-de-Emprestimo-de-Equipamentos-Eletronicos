from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('remove/', views.remove, name='remove'),
]
