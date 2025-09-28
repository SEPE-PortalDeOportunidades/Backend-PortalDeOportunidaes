from django.db import models
from . import *

class Oportunidade(models.Model):
    edital = models.ForeignKey(
        Edital, on_delete=models.PROTECT
    )
    estagio = models.ForeignKey(
        Estagio, on_delete=models.PROTECT
    )
    evento = models.ForeignKey(
        Evento, on_delete=models.PROTECT
    )