from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('detail/<int:funcionarioId>/', views.detail, name='detail'),
    path('edit/<int:funcionarioId>/', views.edit, name='edit'),
    path('remove/<int:funcionarioId>/', views.remove, name='remove'),
]
