from django.db import models
from django.contrib.auth.models import User

class Funcionario(User):
    class Cargo(models.IntegerChoices):
        FUNCIONARIO = 1, 'Funcionario'
        ESTAGIARIO = 2, 'Estagiario'
        OUTRO = 3, 'Outro'

    cargo = models.IntegerField(
        choices=Cargo.choices,
        default=Cargo.OUTRO,
    )
