from django.contrib import admin
from core.PortalDeOportunidades.models import Edital

@admin.register(Edital)
class AdminEdital(admin.ModelAdmin):
    list_display = ("descricao", "numero_edital")
    search_fields = ("descricao", "numero_edital")
    ordering = ("-id",)