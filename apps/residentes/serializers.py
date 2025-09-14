from rest_framework import serializers
from .models import Residente

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = [
            'id','nombre','apellidos','fecha_nacimiento','telefono','correo',
            'dni','sexo','tipo','residencia','activo','fecha_creacion','actualizado'
        ]