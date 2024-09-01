from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'cargo', 'telefone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu Email'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Telefone'})
        }
        labels = {
            'username': 'Nome',
            'email': 'Endereço de Email',
            'cargo': 'Cargo',
            'telefone': 'Telefone'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('senha_padrao123')
        if commit:
            user.save()
        return user
