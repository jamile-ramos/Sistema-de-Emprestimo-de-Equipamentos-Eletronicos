from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    status = models.PositiveIntegerField(choices=[(1, 'Disponível'), (2, 'Emprestado'), (3, 'Em Manutenção')], default=1)

    def __str__(self):
        return self.nome
 
    def emprestar(self):
        if self.status == 1:
            self.status = 2
            self.save()
        else:
            raise ValueError('Equipamento não disponível para empréstimo')
    
    def devolver(self):
        if self.status == 2:
            self.status = 1
            self.save()
        else:
            raise ValueError('Equipamento não está emprestado')

    def iniciarManutencao(self):
        if self.status == 1:
            self.status = 3
            self.save()

    def concluirManutencao(self):
        if self.status == 3:
            self.status = 1
            self.save()
        else:
            raise ValueError('Equipamento não está em manutenção')
