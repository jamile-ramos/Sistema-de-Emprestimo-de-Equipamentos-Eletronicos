from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'cargo', 'password']
        labels = {
            'username': 'Nome',
            'email':'Endereço de Email',
            'cargo':'Cargo',
            'password':'Senha'            
        }