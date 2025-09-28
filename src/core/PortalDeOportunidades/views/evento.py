from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import EventoSerializer
from core.PortalDeOportunidades.models import Evento

class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer