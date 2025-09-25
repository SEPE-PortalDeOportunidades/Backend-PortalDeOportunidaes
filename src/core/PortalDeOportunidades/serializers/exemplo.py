from rest_framework import serializers

from core.PortalDeOportunidades.models import Exemplo

class ExemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplo
        fields = '__all__'