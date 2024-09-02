from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add/', views.add, name='emprestimoAdd'),
    path('detail/<int:emprestimoId>/', views.detail, name='emprestimoDetail'),
    path('edit/<int:emprestimoId>/', views.edit, name='emprestimoEdit'),
    path('remove/<int:emprestimoId>/', views.remove, name='emprestimoRemove'),
    path('list/', views.list, name='emprestimoList')
]
