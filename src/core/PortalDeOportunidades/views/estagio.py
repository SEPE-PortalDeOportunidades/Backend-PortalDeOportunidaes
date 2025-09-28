from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import EstagioSerializer
from core.PortalDeOportunidades.models import Estagio

class EstagioViewSet(ModelViewSet):
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer