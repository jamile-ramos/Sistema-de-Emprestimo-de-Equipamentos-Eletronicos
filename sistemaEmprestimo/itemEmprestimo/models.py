from django.db import models

class ItemEmprestimo(models.Model):
    emprestimo = models.ForeignKey('emprestimo.Emprestimo', on_delete=models.CASCADE)
    equipamento = models.ForeignKey('equipamento.Equipamento', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantidade}x {self.equipamento} para o empréstimo {self.emprestimo.id}"