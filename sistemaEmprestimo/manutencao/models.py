from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now
from equipamento.models import Equipamento
from funcionario.models import Funcionario

# Create your models here.

class Manutencao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    descricao = models.TextField()
    dataInicio = models.DateTimeField(default=now, null=True, blank=True)
    dataConclusao = models.DateTimeField(null=True, blank=True)
    manutentor = models.CharField(max_length=100)
    observacoesDeConclusao = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=[
        (1, 'Concluído'),
        (2, 'Em Andamento'),
        (3, 'Incompleto')
    ], default=2)

    def concluir_manutencao(self, status, observacoes=None):
        self.dataConclusao = datetime.now()
        self.status = status
        if observacoes:
            self.observacoesDeConclusao = observacoes
        self.equipamento.alterar_status(1)  # Retornar o equipamento ao status disponível
        self.save()

    def save(self, *args, **kwargs):
        # Se for uma nova manutenção, marcar o equipamento como "Em Manutenção"
        if not self.pk:
            self.equipamento.alterar_status(3)
        super().save(*args, **kwargs)
