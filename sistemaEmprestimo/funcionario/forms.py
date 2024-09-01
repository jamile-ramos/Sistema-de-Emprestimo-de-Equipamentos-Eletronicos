from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'cargo']
        labels = {
            'username': 'Nome',
            'email': 'Endereço de Email',
            'cargo': 'Cargo',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('senha_padrao123')
        if commit:
            user.save()
        return user
