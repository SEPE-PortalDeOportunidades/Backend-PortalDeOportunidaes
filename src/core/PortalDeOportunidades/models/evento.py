from django.db import models

class Evento(models.Model):
    descricao = models.CharField(max_length=250)
    data = models.DateField()
    palestrante = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.descricao} - {self.palestrante}"