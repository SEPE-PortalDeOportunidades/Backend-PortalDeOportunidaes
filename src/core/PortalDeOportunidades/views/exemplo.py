from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import ExemploSerializer
from core.PortalDeOportunidades.models import Exemplo

class ExemploViewSet(ModelViewSet):
    queryset = Exemplo.objects.all()
    serializer_class = ExemploSerializer