from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status  # ← status está aquí
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
import mercadopago

# Create your views here.

# Tu token de prueba de MercadoPago
TEST_ACCESS_TOKEN = "TEST-4808582478261471-112323-2a8c7d4d52f4b5c6d7e8f9a0b1c2d3e4-123456789"  # Reemplazar con tu token real
sdk = mercadopago.SDK(TEST_ACCESS_TOKEN)


class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all().order_by('id')
    serializer_class = AvisoSerializer
    permission_classes = [IsAuthenticated]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('id')
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().order_by('id')
    serializer_class = VisitaSerializer
    permission_classes = [IsAuthenticated]

class ConceptoPagoViewSet(viewsets.ModelViewSet):
    queryset = ConceptoPago.objects.all().order_by('id')
    serializer_class = ConceptoPagoSerializer
    permission_classes = [IsAuthenticated]

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all().order_by('id')
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]

#implementada por claude IA

    @action(detail=True, methods=['post'])
    def iniciar_pago(self, request, pk=None):
        """Endpoint para iniciar proceso de pago"""
        factura = self.get_object()
        
        # Verificar si la factura ya está pagada
        if factura.estado == 'pagada':
            return Response(
                {"error": "Esta factura ya está pagada"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Crear preferencia de pago en MercadoPago
            preference_data = {
                "items": [{
                    "title": f"Pago Factura #{factura.id}",
                    "description": factura.descripcion,
                    "quantity": 1,
                    "unit_price": float(factura.monto_total),
                    "currency_id": "BOB"  # Bolivianos
                }],
                "payer": {
                    "email": "test_user_123@testuser.com"  # Email de prueba
                },
                "external_reference": str(factura.id),
                "back_urls": {
                    "success": "myapp://payment/success",
                    "failure": "myapp://payment/failure", 
                    "pending": "myapp://payment/pending"
                },
                "auto_return": "approved"
            }
            
            # Crear preferencia en MercadoPago
            preference = sdk.preference().create(preference_data)
            
            if preference["status"] == 201:
                # Crear registro de pago en tu BD
                pago = Pago.objects.create(
                    factura=factura,
                    monto=factura.monto_total,
                    preference_id=preference["response"]["id"],
                    estado='pending'
                )
                
                return Response({
                    "success": True,
                    "pago_id": pago.id,
                    "preference_id": preference["response"]["id"],
                    "init_point": preference["response"]["init_point"],  # URL para Flutter
                    "sandbox_init_point": preference["response"]["sandbox_init_point"]
                })
            else:
                return Response(
                    {"error": "Error al crear preferencia de pago"}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
        except Exception as e:
            return Response(
                {"error": f"Error en el proceso de pago: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['post'])
    def webhook_pago(self, request):
        """Webhook para recibir notificaciones de MercadoPago"""
        try:
            # Obtener datos del webhook
            payment_id = request.data.get("data", {}).get("id")
            
            if payment_id:
                # Consultar el pago en MercadoPago
                payment_info = sdk.payment().get(payment_id)
                
                if payment_info["status"] == 200:
                    payment = payment_info["response"]
                    external_reference = payment.get("external_reference")
                    
                    if external_reference:
                        # Buscar la factura y el pago
                        factura = get_object_or_404(Factura, id=external_reference)
                        pago = Pago.objects.filter(factura=factura).first()
                        
                        if pago:
                            # Actualizar estado del pago
                            pago.payment_id = str(payment_id)
                            pago.estado = payment.get("status", "pending")
                            pago.metodo_pago = payment.get("payment_method_id", "")
                            pago.save()
                            
                            # Actualizar estado de la factura
                            if payment.get("status") == "approved":
                                factura.estado = 'pagada'
                                factura.save()
            
            return Response({"status": "ok"})
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all().order_by('id')
    serializer_class = DetalleFacturaSerializer
    permission_classes = [IsAuthenticated]

#implementada por claude IA
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all().order_by('-fecha_pago')
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]    