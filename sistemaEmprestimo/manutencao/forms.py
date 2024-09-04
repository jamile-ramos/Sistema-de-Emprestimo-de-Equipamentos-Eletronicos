from django import forms
from .models import Manutencao
from equipamento.models import Equipamento

class ManutencaoFormRoot(forms.ModelForm):
    equipamento = forms.ModelChoiceField(
        queryset=Equipamento.objects.filter(status=1),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )  
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'descricao', 'manutentor']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'manutentor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
        }

class ManutencaoFormFuncionario(forms.ModelForm):
    equipamento = forms.ModelChoiceField(
        queryset=Equipamento.objects.filter(status=1),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
     
    class Meta:
        model = Manutencao
        fields = ['equipamento', 'descricao', 'manutentor']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'manutentor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
        }

class ManutencaoFormEdit(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['descricao', 'manutentor']
        widgets = {
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