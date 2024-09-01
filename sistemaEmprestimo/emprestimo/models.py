from django.db import models

class Emprestimo(models.Model):
    
    class TipoDoPrestamista(models.IntegerChoices):
        ALUNO = 1, 'Aluno'
        PROFESSOR = 2, 'Professor'
        FUNCIONARIO = 3, 'Funcionário'
        OUTRO = 4, 'Outro'
        
    class Status(models.IntegerChoices):
        CONCLUIDO = 1, 'Devolvido'
        ANDAMENTO = 2, 'Em Andamento'
        INCOMPLETO = 3, 'Atrasado'
    
    prestamista = models.CharField(max_length=50)
    tipoDoPrestamista = models.IntegerField(choices=TipoDoPrestamista.choices, default=TipoDoPrestamista.OUTRO)
    sala = models.IntegerField()  # Adicionado parênteses
    curso = models.CharField(max_length=20)
    semestre = models.IntegerField()  # Adicionado parênteses
    dataEmprestimo = models.DateTimeField()  # Adicionado parênteses
    dataDevolucao = models.DateTimeField(null=True, blank=True)  # Adicionado parênteses e permite valor nulo
    observacoesDeDevolucao = models.CharField(max_length=255, blank=True)  # Adicionado parênteses e comprimento
    status = models.IntegerField(choices=Status.choices, default=Status.ANDAMENTO)  # Adicionado valor padrão

    def __str__(self):
        return f"{self.prestamista} - {self.get_status_display()}"
