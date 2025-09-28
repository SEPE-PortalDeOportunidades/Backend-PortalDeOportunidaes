from django.db import models

class Estagio(models.Model):
    descricao = models.CharField(max_length=250)
    local = models.CharField(max_length=300)
    carga_horaria = models.CharField(max_length=80)
    salario = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao