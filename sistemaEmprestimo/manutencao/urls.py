from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_manutencoes, name='listar_manutencoes'),
    path('criar/', views.criar_manutencao, name='criar_manutencao'),
    path('editar/<int:pk>/', views.editar_manutencao, name='editar_manutencao'),
    path('detalhar/<int:pk>/', views.detalhar_manutencao, name='detalhar_manutencao'),
    path('concluir/<int:pk>/', views.concluir_manutencao, name='concluir_manutencao'),
    path('remover/<int:pk>/', views.apagar_manutencao, name='apagar_manutencao'),
]
