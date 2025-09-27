from django.db import models
from apps.residentes.models import Residente    
from apps.areas.models import AreaComun
from apps.cuentas.models import Usuario
# Create your models here.

class Aviso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
    hora = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'

    def __str__(self):
        return self.titulo
    
class Reserva(models.Model): 
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaComun, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"Reserva de {self.residente} en {self.area} el {self.fecha_reserva}"

class Visita(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    fecha_llegada = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'

    def __str__(self):
        return f"Visita de {self.nombre} al residente {self.residente}"
  
class ConceptoPago(models.Model):
    
    #factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Concepto de Pago'
        verbose_name_plural = 'Conceptos de Pago'

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    concepto = models.ManyToManyField(ConceptoPago, through='DetalleFactura')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.TextField(max_length=100)
    fecha_limite = models.DateField(null=True, blank=True)
    fecha_emision = models.DateField(null=True, blank=True)
    descripcion = models.TextField(max_length=200)
    class Meta:
        ordering = ['id']
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"Factura {self.id} para {self.residente}"
    
    
class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    concepto = models.ForeignKey(ConceptoPago, on_delete=models.CASCADE)

    def __str__(self):
        return f"Detalle de {self.concepto.nombre} para Factura {self.factura.id}"
      