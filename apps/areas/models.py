from django.db import models

class AreaComun(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Área Común'
        verbose_name_plural = 'Áreas Comunes'

    def __str__(self):
        return self.nombre

class Regla(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    areas = models.ManyToManyField(AreaComun, related_name='reglas', blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Regla'
        verbose_name_plural = 'Reglas'

    def __str__(self):
        return self.nombre


