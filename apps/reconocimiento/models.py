from django.db import models

# Create your models here.
# apps/reconocimiento/models.py
class RostroResidente(models.Model):
    residente = models.OneToOneField('residentes.Residente', on_delete=models.CASCADE)
    face_encoding = models.JSONField()
    imagen_referencia = models.ImageField(upload_to='rostros/')
    calidad_imagen = models.FloatField()
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

class RegistroAccesoFacial(models.Model):
    residente = models.ForeignKey('residentes.Residente', on_delete=models.SET_NULL, null=True)
    resultado = models.CharField(max_length=20)  # autorizado/denegado
    confianza = models.FloatField()
    imagen_acceso = models.ImageField(upload_to='accesos/')
    timestamp = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)