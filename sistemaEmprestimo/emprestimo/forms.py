from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['prestamista', 'tipoDoPrestamista', 'sala', 'curso', 'semestre', 'dataEmprestimo', 'dataDevolucao', 'observacoesDeDevolucao', 'status']
        widgets = {
            'prestamista': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}),
            'tipoDoPrestamista': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.NumberInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Curso'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'dataEmprestimo': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'dataDevolucao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'observacoesDeDevolucao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'prestamista': 'Nome',
            'tipoDoPrestamista': 'Tipo de Prestamista',
            'sala': 'Sala',
            'curso': 'Curso',
            'semestre': 'Semestre',
            'dataEmprestimo': 'Data do Empréstimo',
            'dataDevolucao': 'Data de Devolução',
            'observacoesDeDevolucao': 'Observações de Devolução',
            'status': 'Status',
        }