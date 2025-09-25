from core.PortalDeOportunidades import views

from rest_framework.routers import DefaultRouter
from core.PortalDeOportunidades import views

router = DefaultRouter()

router.register(r'exemplo', views.ExemploViewSet, basename='Exemplo')
