from django.db import models
from conta.models import Usuario

class Funcionario(Usuario):
    class Cargo(models.IntegerChoices):
        FUNCIONARIO = 1, 'Funcionario'
        ESTAGIARIO = 2, 'Estagiario'
        OUTRO = 3, 'Outro'

    cargo = models.IntegerField(
        choices=Cargo.choices,
        default=Cargo.OUTRO,
    )
    
