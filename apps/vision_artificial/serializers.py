from rest_framework import serializers
from .models import logReconocimiento

class LogReconocimientoSerializer(serializers.ModelSerializer):
    nombre_residente = serializers.SerializerMethodField()
    apellido_residente = serializers.SerializerMethodField()
    foto_residente = serializers.SerializerMethodField()

    def get_nombre_residente(self, obj):
        try:
            if obj.residente:
                return obj.residente.nombre or ""
            return ""
        except:
            return ""

    def get_apellido_residente(self, obj):
        try:
            if obj.residente:
                return obj.residente.apellido or ""
            return ""
        except:
            return ""

    def get_foto_residente(self, obj):
        try:
            if obj.residente and hasattr(obj.residente, 'foto_perfil'):
                return obj.residente.foto_perfil or ""
            return ""
        except:
            return ""

    class Meta:
        model = logReconocimiento
        fields = [
            'id',
            'residente',
            'fecha_hora',
            'foto_ruta',
            'descripcion',
            'coincidencia',
            'nombre_residente',
            'apellido_residente',
            'foto_residente',
        ]

