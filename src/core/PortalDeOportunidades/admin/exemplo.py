from django.contrib import admin
from core.PortalDeOportunidades.models import Exemplo

@admin.register(Exemplo)
class AdminExemplo(admin.ModelAdmin):
    list_display = ("nome", "idade")
    search_fields = ("nome", "idade")
    ordering = ("-id",)