from django import forms
from .models import Manutencao

class ManutencaoFormRoot(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'descricao', 'manutentor']
        widgets = {
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'manutentor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
        }

class ManutencaoFormFuncionario(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'descricao', 'manutentor']
        widgets = {
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'manutentor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
        }

class ManutencaoConclusaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['status', 'observacoesDeConclusao']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacoesDeConclusao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
        }
        labels = {
            'observacoesDeConclusao':'Observacões de Conclusão'
        }