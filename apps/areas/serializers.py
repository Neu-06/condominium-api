from rest_framework import serializers
from .models import AreaComun, Regla, Horario


class HorarioSerializer(serializers.ModelSerializer):
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)
    class Meta:
        model = Horario
        fields = [
            "id",
            "area",
            "area_nombre",
            "dia_semana",
            "hora_apertura",
            "hora_cierre",
            "activo",
            "creado",
            "actualizado",
        ]


class ReglaSerializer(serializers.ModelSerializer):
    areas_ids = serializers.PrimaryKeyRelatedField(
        many=True, source="areas", queryset=AreaComun.objects.all(), required=False
    )

    class Meta:
        model = Regla
        fields = [
            "id",
            "nombre",
            "descripcion",
            "areas_ids",
            "activo",
            "creado",
            "actualizado",
        ]


class AreaComunSerializer(serializers.ModelSerializer):
    reglas_ids = serializers.PrimaryKeyRelatedField(
        many=True, source="reglas", queryset=Regla.objects.all(), required=False
    )
    reglas = ReglaSerializer(many=True, read_only=True)
    horarios = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = AreaComun
        fields = [
            "id",
            "nombre",
            "descripcion",
            "requiere_reserva",
            "capacidad_maxima",
            "costo_reserva",
            "tiempo_reserva_minima",
            "tiempo_reserva_maxima",
            "estado",
            "reglas_ids",
            "reglas",
            "horarios",
            "activo",
            "creado",
            "actualizado",
        ]


class HorarioCreateSerializer(serializers.ModelSerializer):
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)  
    class Meta:
        model = Horario

    fields = [
        "area",
        "dia_semana",
        "hora_apertura",
        "hora_cierre",
        "activo",
    ]
