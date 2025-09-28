from rest_framework import serializers
from core.PortalDeOportunidades.models import Estagio

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = '__all__'