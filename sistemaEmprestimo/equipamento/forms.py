from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'codigo', 'marca']
        widgets = {
            'status': forms.Select(
                choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Em Manutenção')],
                attrs={'class': 'form-control'}
            ),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do equipamento'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o código'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a marca do Equipamento'}),
        }
        labels = {
            'nome': 'Nome do Equipamento',
            'codigo': 'Código',
            'marca': 'Marca',
            'status': 'Status',
        }

class AtualizarStatusForm(forms.Form):
    novo_status = forms.ChoiceField(
        choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Em Manutenção')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
