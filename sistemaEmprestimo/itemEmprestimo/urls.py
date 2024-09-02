from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add/', views.add, name='itemEmprestimoAdd'),
    path('detail/<int:itemEmprestimoId>/', views.detail, name='itemEmprestimoDetail'),
    path('edit/<int:itemEmprestimoId>/', views.edit, name='itemEmprestimoEdit'),
    path('remove/<int:itemEmprestimoId>/', views.remove, name='itemEmprestimoRemove'),
    path('list/', views.list, name='itemEmprestimoList')
]
