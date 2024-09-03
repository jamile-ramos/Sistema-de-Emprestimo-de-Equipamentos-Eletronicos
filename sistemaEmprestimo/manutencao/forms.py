from django import forms
from .models import Manutencao

class ManutencaoFormRoot(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'funcionario', 'descricao', 'manutentor']

class ManutencaoFormFuncionario(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'descricao', 'manutentor']

class ManutencaoConclusaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['status', 'observacoesDeConclusao']