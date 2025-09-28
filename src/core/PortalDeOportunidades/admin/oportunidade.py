from django.contrib import admin
from core.PortalDeOportunidades.models import Oportunidade

@admin.register(Oportunidade)
class AdminOportunidade(admin.ModelAdmin):
    list_display = ("edital", "estagio", "evento")
    ordering = ("-id",)