from django.db import models
from conta.models import Usuario

class Funcionario(Usuario):
    class Cargo(models.IntegerChoices):
        ROOT = 1, 'Root'
        FUNCIONARIO = 2, 'Funcionario'
        ESTAGIARIO = 3, 'Estagiario'
        OUTRO = 4, 'Outro'

    cargo = models.IntegerField(
        choices=Cargo.choices,
        default=Cargo.OUTRO,
    )
    
