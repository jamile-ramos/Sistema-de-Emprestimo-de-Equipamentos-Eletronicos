from rest_framework import viewsets
from .serializers import UsuarioSerializer, FuncionarioSerializer, EquipamentoSerializer, EmprestimoSerializer, ManutencaoSerializer, ItemEmprestimoSerializer,  EmprestimoDetailSerializer, ManutencaoDetailSerializer, ItemEmprestimoDetailSerializer
from equipamento.models import Equipamento
from funcionario.models import Funcionario
from emprestimo.models import Emprestimo
from manutencao.models import Manutencao
from itemEmprestimo.models import ItemEmprestimo
from conta.models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EmprestimoDetailSerializer
        return EmprestimoSerializer

    serializer_class = EmprestimoSerializer

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ManutencaoDetailSerializer
        return ManutencaoSerializer
    serializer_class = ManutencaoSerializer

class ItemEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = ItemEmprestimo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ItemEmprestimoDetailSerializer
        return ItemEmprestimoSerializer
    
    serializer_class = ItemEmprestimoSerializer
