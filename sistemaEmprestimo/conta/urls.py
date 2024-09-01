from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createUser, name='createUser'),  
    path('logout/', views.logout_view, name='logout')
]
