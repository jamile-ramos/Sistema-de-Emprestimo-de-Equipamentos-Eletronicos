from django import forms
from .models import Emprestimo
from equipamento.models import Equipamento

class EmprestimoForm(forms.ModelForm):
    equipamentos = forms.ModelMultipleChoiceField(
        queryset=Equipamento.objects.all().filter(status=1),  
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
            
    class Meta:
        model = Emprestimo
        fields = ['requisitante', 'tipoDoRequisitante', 'sala', 'curso', 'dataEmprestimo', 'dataDevolucao', 'equipamentos', 'observacoesDeDevolucao', 'status']
        widgets = {
            'requisitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'tipoDoRequisitante': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sala 1, sala da diretoria, etc'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o curso'}),
            'dataEmprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dataDevolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observacoesDeDevolucao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'requisitante': 'Nome do requisitante',
            'tipoDoRequisitante': 'Tipo de requisitante',
            'sala': 'Sala',
            'curso': 'Curso (Obrigatório apenas para alunos)',
            'dataEmprestimo': 'Data do Empréstimo',
            'dataDevolucao': 'Data de Devolução',
            'observacoesDeDevolucao': 'Observações de Devolução',
            'status': 'Status',
        }
        

class EmprestimoEditForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['requisitante', 'tipoDoRequisitante', 'sala', 'curso', 'dataEmprestimo', 'dataDevolucao', 'observacoesDeDevolucao', 'status']
        widgets = {
            'requisitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'tipoDoRequisitante': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sala 1, sala da diretoria, etc'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o curso'}),
            'dataEmprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dataDevolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observacoesDeDevolucao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'requisitante': 'Nome do requisitante',
            'tipoDoRequisitante': 'Tipo de requisitante',
            'sala': 'Sala',
            'curso': 'Curso (Obrigatório apenas para alunos)',
            'dataEmprestimo': 'Data do Empréstimo',
            'dataDevolucao': 'Data de Devolução',
            'observacoesDeDevolucao': 'Observações de Devolução',
            'status': 'Status',
        }