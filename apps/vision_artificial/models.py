from django.db import models
from apps.residentes.models import Residente

class logReconocimiento(models.Model):
    residente = models.ForeignKey(
        Residente, on_delete=models.SET_NULL, null=True, blank=True
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)
    foto_ruta = models.URLField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    coincidencia = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.residente:
            return f"{self.residente} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}"
        return f"Desconocido - {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}"

