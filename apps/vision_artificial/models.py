from django.db import models

class logReconocimiento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo_evento = models.CharField(max_length=50)  # e.g., 'ingreso', 'salida', 'anomalía'
    imagen = models.ImageField(upload_to='reconocimiento_facial/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_evento} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}"
