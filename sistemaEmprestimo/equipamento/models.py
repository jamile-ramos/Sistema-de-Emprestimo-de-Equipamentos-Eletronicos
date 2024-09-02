from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    status = models.PositiveIntegerField(choices=[(1, 'Disponível'), (2, 'Indisponível'), (3, 'Em Manutenção')], default=1)

    def __str__(self):
        return self.nome
