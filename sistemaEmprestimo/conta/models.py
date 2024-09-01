from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    telefone = models.CharField(max_length=20)
