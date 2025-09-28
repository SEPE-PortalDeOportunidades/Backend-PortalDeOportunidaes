from core.PortalDeOportunidades import views

from rest_framework.routers import DefaultRouter
from core.PortalDeOportunidades import views

router = DefaultRouter()

router.register(r'curso', views.CursoViewSet)
router.register(r'evento', views.EventoViewSet)
router.register(r'edital', views.EditalViewSet)
router.register(r'estagio', views.EstagioViewSet)
router.register(r'oportunidade', views.OportunidadeViewSet)
