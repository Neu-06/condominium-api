from rest_framework import serializers
from .models import *

class RostroResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RostroResidente
        fields = '__all__'

class RegistroAccesoFacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAccesoFacial
        fields = '__all__'
