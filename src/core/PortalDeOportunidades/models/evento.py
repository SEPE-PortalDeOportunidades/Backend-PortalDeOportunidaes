from django.db import models
from django.utils import timezone

class Evento(models.Model):
    descricao = models.CharField(max_length=250)
    data = models.DateTimeField(default=timezone.now)
    palestrante = models.CharField(max_length=200)
    local = models.CharField(max_length=200, default='IFC')
    
    def __str__(self):
        return f"{self.descricao} - {self.palestrante} - {self.local}"