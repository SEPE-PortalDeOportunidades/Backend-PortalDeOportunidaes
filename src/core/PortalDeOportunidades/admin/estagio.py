from django.contrib import admin
from core.PortalDeOportunidades.models import Estagio

@admin.register(Estagio)
class AdminEstagio(admin.ModelAdmin):
    ordering = ("-id",)