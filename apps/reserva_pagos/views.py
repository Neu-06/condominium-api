from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


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

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all().order_by('id')
    serializer_class = DetalleFacturaSerializer
    permission_classes = [IsAuthenticated]