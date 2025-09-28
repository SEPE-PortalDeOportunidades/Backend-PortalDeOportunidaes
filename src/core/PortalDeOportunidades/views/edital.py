from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import EditalSerializer
from core.PortalDeOportunidades.models import Edital

class EditalViewSet(ModelViewSet):
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer