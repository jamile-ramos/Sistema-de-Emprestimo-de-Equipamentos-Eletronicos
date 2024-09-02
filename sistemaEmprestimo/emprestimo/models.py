from django.db import models
from django.utils import timezone

class Emprestimo(models.Model):
    
    class TipoDoRequisitante(models.IntegerChoices):
        ALUNO = 1, 'Aluno'
        PROFESSOR = 2, 'Professor'
        FUNCIONARIO = 3, 'Funcionário'
        OUTRO = 4, 'Outro'
        
    class Status(models.IntegerChoices):
        CONCLUIDO = 1, 'Devolvido'
        ANDAMENTO = 2, 'Em Andamento'
        INCOMPLETO = 3, 'Atrasado'
    
    requisitante = models.CharField(max_length=50)
    tipoDoRequisitante = models.IntegerField(choices=TipoDoRequisitante.choices, default=TipoDoRequisitante.OUTRO)
    sala = models.CharField(max_length=50)
    curso = models.CharField(max_length=20, null=True)
    dataEmprestimo = models.DateField(default=timezone.now) 
    dataDevolucao = models.DateField(null=True, blank=True)
    observacoesDeDevolucao = models.CharField(max_length=255, blank=True)  
    status = models.IntegerField(choices=Status.choices, default=Status.ANDAMENTO) 
    
    # Relacionamento de muitos para um com Funcionario
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.requisitante} - {self.get_status_display()}"
