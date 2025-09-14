from django.db import models


class Residente(models.Model):
    SEXO_CHOICES = (("M", "Masculino"), ("F", "Femenino"))
    TIPO_CHOICES = (
        ("PROPIETARIO", "Propietario"),
        ("INQUILINO", "Inquilino"),
        ("HABITANTE", "Habitante"),
    )

    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    correo = models.EmailField(max_length=150, blank=True)
    dni = models.CharField(max_length=30, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    residencia = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
