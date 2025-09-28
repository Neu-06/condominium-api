from rest_framework import serializers
from .models import *

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = [
            'id','nombre','apellidos','fecha_nacimiento','telefono','correo',
            'dni','sexo','tipo','residencia','foto_perfil','activo','fecha_creacion','actualizado'
        ]

class ResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residencia
        fields = ['numero','direccion','tipo','num_habitaciones','num_residentes']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id','marca','modelo','matricula','color','tipo','residente']
        
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id','nombre','tipo','raza','residente']

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = [
            'id','nombre','apellidos','dni','telefono','residente',
            'foto_referencial','fecha_visita','hora_entrada','hora_salida'
        ]
