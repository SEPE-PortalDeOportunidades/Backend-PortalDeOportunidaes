from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    area = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome} - {self.area}"

