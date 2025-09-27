from rest_framework import serializers
from .models import *

class PrediccionMorosidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediccionMorosidad
        fields = '__all__'

class EventoAnomalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoAnomalidad
        fields = '__all__'

class EstadisticaDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticaDiaria
        fields = '__all__'
