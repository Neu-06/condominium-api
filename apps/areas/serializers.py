from rest_framework import serializers
from .models import AreaComun, Regla

class ReglaSerializer(serializers.ModelSerializer):
    areas_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        source='areas',
        queryset=AreaComun.objects.all(),
        required=False
    )

    class Meta:
        model = Regla
        fields = ['id','nombre','descripcion','activo','areas_ids','creado','actualizado']

class AreaComunSerializer(serializers.ModelSerializer):
    reglas_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        source='reglas',
        queryset=Regla.objects.all(),
        required=False
    )
    reglas = ReglaSerializer(many=True, read_only=True)

    class Meta:
        model = AreaComun
        fields = ['id','nombre','descripcion','activo','reglas_ids','reglas','creado','actualizado']