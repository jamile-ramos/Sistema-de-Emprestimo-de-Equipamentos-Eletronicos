from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='funcionarioIndex'),
    path('add/', views.add, name='funcionarioAdd'),
    path('detail/<int:funcionarioId>/', views.detail, name='funcionarioDetail'),
    path('edit/<int:funcionarioId>/', views.edit, name='funcionarioEdit'),
    path('remove/<int:funcionarioId>/', views.remove, name='funcionarioRemove'),
    path('list/', views.list, name='funcionarioList')
]
