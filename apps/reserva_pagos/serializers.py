from rest_framework import serializers
from .models import Aviso, Reserva, Visita, ConceptoPago, Factura, DetalleFactura,Pago

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields =['id', 'usuario', 'titulo', 'mensaje', 'fecha', 'hora']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'residente', 'area', 'nombre', 'descripcion']

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = ['id','residente', 'nombre', 'apellido', 'dni', 'genero', 'fecha_llegada']

class ConceptoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoPago
        fields = ['id', 'nombre', 'monto']

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = ['id', 'factura', 'concepto']

class FacturaSerializer(serializers.ModelSerializer):
    # Para mostrar los detalles dentro de la factura
    conceptos = DetalleFacturaSerializer(many=True, read_only=True, source='detallefactura_set')

    class Meta:
        model = Factura
        fields = [
            'id', 'residente','concepto', 'monto_total', 'estado', 
            'fecha_limite', 'fecha_emision','descripcion','pagos', 
        ]#se agrego pagos 
        
#parte de la implmentacion de claude IA

class PagoSerializer(serializers.ModelSerializer):
    factura_info = FacturaSerializer(source='factura', read_only=True)
    
    class Meta:
        model = Pago
        fields = [
            'id', 'factura', 'factura_info', 'monto', 'estado', 
            'payment_id', 'preference_id', 'metodo_pago', 
            'fecha_pago', 'fecha_actualizacion'
        ]
        
