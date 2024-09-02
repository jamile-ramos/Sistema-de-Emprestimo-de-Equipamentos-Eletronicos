from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['requisitante', 'tipoDoRequisitante', 'sala', 'curso', 'dataEmprestimo', 'dataDevolucao', 'funcionario', 'observacoesDeDevolucao', 'status']
        widgets = {
            'requisitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome'}),
            'tipoDoRequisitante': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sala 1, sala da diretoria, etc'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o curso'}),
            'dataEmprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dataDevolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
            'observacoesDeDevolucao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'requisitante': 'Nome do requisitante',
            'tipoDoRequisitante': 'Tipo de requisitante',
            'sala': 'Sala',
            'curso': 'Curso (Obrigatório apenas para alunos)',
            'semestre': 'Semestre (Obrigatório apenas para alunos)',
            'dataEmprestimo': 'Data do Empréstimo',
            'dataDevolucao': 'Data de Devolução',
            'funcionario': 'Funcionário responsável pelo Empréstimo',
            'observacoesDeDevolucao': 'Observações de Devolução',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Recebe o usuário logado do argumento kwargs
        super(EmprestimoForm, self).__init__(*args, **kwargs)
        if user:
            # Preenche o campo 'funcionario' com o usuário logado
            self.fields['funcionario'].initial = user.funcionario if hasattr(user, 'funcionario') else None

    def clean(self):
        cleaned_data = super().clean()
        tipo_do_requisitante = cleaned_data.get('tipoDoRequisitante')
        semestre = cleaned_data.get('semestre')

        # Verifica se o tipo de requisitante é "Aluno" e o campo semestre está vazio
        if tipo_do_requisitante == 'Aluno' and not semestre:
            self.add_error('semestre', 'O campo "Semestre" é obrigatório quando o tipo de requisitante é "Aluno".')

        return cleaned_data
