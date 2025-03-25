from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, FuncionarioViewSet, EquipamentoViewSet, EmprestimoViewSet, ManutencaoViewSet, ItemEmprestimoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'manutencao', ManutencaoViewSet)
router.register(r'itensEmprestimo', ItemEmprestimoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
