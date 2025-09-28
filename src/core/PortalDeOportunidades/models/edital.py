from django.db import models

class Edital(models.Model):
    descricao = models.CharField(max_length=250)
    numero_edital = models.CharField(max_length=50)
    data_publicacao = models.DateField()
    data_validade = models.DateField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'