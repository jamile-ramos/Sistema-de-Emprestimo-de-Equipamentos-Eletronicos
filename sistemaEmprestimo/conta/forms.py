from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from conta.models import Usuario
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import PasswordChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Digite seu nome'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Digite seu endereço de email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Digite sua senha'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control form-control-user'
            })
        }

