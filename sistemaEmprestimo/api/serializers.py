from rest_framework import serializers
from equipamento.models import Equipamento
from funcionario.models import Funcionario
from emprestimo.models import Emprestimo
from manutencao.models import Manutencao
from itemEmprestimo.models import ItemEmprestimo
from conta.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'telefone', 'first_name', 'last_name', 'email']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'username', 'telefone', 'cargo', 'first_name', 'last_name', 'email']

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = ['id', 'nome', 'codigo', 'marca', 'status']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'requisitante', 'tipoDoRequisitante', 'sala', 'curso', 'dataEmprestimo', 'dataDevolucao', 'observacoesDeDevolucao', 'status', 'funcionario', 'equipamentos']

class EmprestimoDetailSerializer(serializers.ModelSerializer):
    funcionario = serializers.SerializerMethodField()
    equipamentos = serializers.SerializerMethodField()

    class Meta: 
        model = Emprestimo
        fields = ['id', 'requisitante', 'tipoDoRequisitante', 'sala', 'curso', 
                  'dataEmprestimo', 'dataDevolucao', 'observacoesDeDevolucao', 
                  'status', 'funcionario', 'equipamentos']
    
    def get_funcionario(self, obj):
        if obj.funcionario:
            return {
                'id': obj.funcionario.id,
                'nome': obj.funcionario.username,
                'email': obj.funcionario.email  
            }
        return None  

    def get_equipamentos(self, obj):
        if obj.equipamentos.exists():  
            return [
                {
                    'id': equipamento.id,
                    'nome': equipamento.nome,
                    'codigo': equipamento.codigo,
                    'marca': equipamento.marca,
                    'status': equipamento.status
                }
                for equipamento in obj.equipamentos.all()
            ]
        return []
    
class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = ['id', 'equipamento', 'funcionario', 'descricao', 'dataInicio', 'dataConclusao', 'manutentor', 'observacoesDeConclusao', 'status']

class ManutencaoDetailSerializer(serializers.ModelSerializer):
    funcionario = serializers.SerializerMethodField()

    class Meta:
        model = Manutencao
        fields = ['id', 'equipamento', 'funcionario', 'descricao', 'dataInicio', 
                  'dataConclusao', 'manutentor', 'observacoesDeConclusao', 'status']

    def get_funcionario(self, obj):
        return {
            'id': obj.funcionario.id,
            'nome': obj.funcionario.username,
            'email': obj.funcionario.email  
        }


class ItemEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEmprestimo
        fields = ['id', 'quantidade', 'emprestimo', 'equipamento']
        
class ItemEmprestimoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEmprestimo
        fields = ['id', 'quantidade', 'emprestimo', 'equipamento']
        depth = 1

