from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import OportunidadeSerializer
from core.PortalDeOportunidades.models import Oportunidade

class OportunidadeViewSet(ModelViewSet):
    queryset = Oportunidade.objects.all()
    serializer_class = OportunidadeSerializer