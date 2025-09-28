from django.contrib import admin
from core.PortalDeOportunidades.models import Evento

@admin.register(Evento)
class AdminEvento(admin.ModelAdmin):
    ordering = ("-id",)