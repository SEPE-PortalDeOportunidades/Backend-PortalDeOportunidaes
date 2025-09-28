from rest_framework.viewsets import ModelViewSet

from core.PortalDeOportunidades.serializers import CursoSerializer
from core.PortalDeOportunidades.models import Curso

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer