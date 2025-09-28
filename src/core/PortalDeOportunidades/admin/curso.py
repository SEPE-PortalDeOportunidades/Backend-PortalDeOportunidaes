from django.contrib import admin
from core.PortalDeOportunidades.models import Curso

@admin.register(Curso)
class AdminCurso(admin.ModelAdmin):
    list_display = ("nome", "area")
    search_fields = ("nome", "area")
    ordering = ("-id",)