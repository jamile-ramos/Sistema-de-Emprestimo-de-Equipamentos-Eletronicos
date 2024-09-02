from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('criar/', views.criar_equipamento, name='criar_equipamento'),
    path('detalhes/<int:id>/', views.detalhar_equipamento, name='detalhar_equipamento'),
    path('editar/<int:id>/', views.editar_equipamento, name='editar_equipamento'),
    path('deletar/<int:id>/', views.deletar_equipamento, name='deletar_equipamento'),
    path('alterar-status/<int:id>/', views.atualizar_status, name='atualizar_status'),
]