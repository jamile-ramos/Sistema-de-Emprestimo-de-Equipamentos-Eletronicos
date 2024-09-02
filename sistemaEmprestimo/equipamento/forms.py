from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'codigo', 'marca']
        widgets = {
            'status': forms.CheckboxSelectMultiple(
                choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Em Manutenção')]
            )
        }

class AtualizarStatusForm(forms.Form):
    novo_status = forms.ChoiceField(choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Em Manutenção')])