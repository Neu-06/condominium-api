from django.db import models

# Create your models here.
# apps/analytics/models.py
class PrediccionMorosidad(models.Model):
    residente = models.ForeignKey('residentes.Residente', on_delete=models.CASCADE)
    probabilidad_morosidad = models.FloatField()
    nivel_riesgo = models.CharField(max_length=10)
    factores_riesgo = models.JSONField()
    fecha_prediccion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField()

class EventoAnomalidad(models.Model):
    tipo_anomalia = models.CharField(max_length=50)  # horario_inusual, multiple_intentos
    descripcion = models.TextField()
    datos_evento = models.JSONField()
    nivel_severidad = models.IntegerField()  # 1-10
    timestamp = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)

class EstadisticaDiaria(models.Model):
    fecha = models.DateField(unique=True)
    total_accesos = models.IntegerField(default=0)
    accesos_autorizados = models.IntegerField(default=0)
    visitantes_registrados = models.IntegerField(default=0)
    vehiculos_ingresados = models.IntegerField(default=0)
    anomalias_detectadas = models.IntegerField(default=0)