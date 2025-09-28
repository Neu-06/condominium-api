from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Reserva, ConceptoPago, Factura, DetalleFactura, Pago
from .serializers import (
    ReservaSerializer, ConceptoPagoSerializer, FacturaSerializer,
    DetalleFacturaSerializer, PagoSerializer
)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('id')
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

class ConceptoPagoViewSet(viewsets.ModelViewSet):
    queryset = ConceptoPago.objects.all().order_by('id')
    serializer_class = ConceptoPagoSerializer
    permission_classes = [IsAuthenticated]

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all().order_by('id')
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleFacturaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = DetalleFactura.objects.all().order_by('id')
        factura_id = self.request.query_params.get('factura')
        if factura_id:
            queryset = queryset.filter(factura_id=factura_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        detalle = self.get_object()
        factura = detalle.factura
        response = super().destroy(request, *args, **kwargs)
        # Actualiza el monto_total de la factura después de eliminar el detalle
        total = sum(d.monto for d in factura.detalles.all())
        factura.monto_total = total
        factura.save()
        return response

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all().order_by('-fecha_pago')
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
