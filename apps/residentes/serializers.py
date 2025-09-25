from rest_framework import serializers
from .models import *

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = [
            'id','nombre','apellidos','fecha_nacimiento','telefono','correo',
            'dni','sexo','tipo','residencia','activo','fecha_creacion','actualizado'
        ]
class ResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residencia
        fields = ['numero','direccion','tipo','num_habitaciones','num_residentes']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id','marca','modelo','matricula','color','tipo','imagen_vehiculo','residente']
        
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id','nombre','tipo','raza','residente']

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = ['id','nombre','apellidos','dni','telefono','residente','fecha_visita','hora_entrada','hora_salida','foto_ingreso']
        
class AutorizacionVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacionVisita
        fields = ['id','residente_autorizador','visitante_esperado','documento_esperado','fecha_autorizacion','fecha_expiracion','utilizada']        