from rest_framework import serializers
from core.PortalDeOportunidades.models import Oportunidade

class OportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunidade
        fields = '__all__'