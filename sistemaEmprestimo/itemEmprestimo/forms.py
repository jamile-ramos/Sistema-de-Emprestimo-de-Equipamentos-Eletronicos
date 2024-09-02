from django import forms
from .models import ItemEmprestimo

class ItemEmprestimoForm(forms.ModelForm):
    class Meta:
        model = ItemEmprestimo  
        fields = ['emprestimo', 'equipamento', 'quantidade']
