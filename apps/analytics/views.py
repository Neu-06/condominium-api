from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PrediccionMorosidad, EventoAnomalidad, EstadisticaDiaria
from .serializers import (
    PrediccionMorosidadSerializer, 
    EventoAnomalidadSerializer, 
    EstadisticaDiariaSerializer
)

class PrediccionMorosidadViewSet(viewsets.ModelViewSet):
    #
    #ViewSet para gestionar las predicciones de morosidad.
    #
    queryset = PrediccionMorosidad.objects.all()
    serializer_class = PrediccionMorosidadSerializer
    permission_classes = [IsAuthenticated]

class EventoAnomalidadViewSet(viewsets.ModelViewSet):
    #
    #ViewSet para gestionar los eventos de anomalías.
    #
    queryset = EventoAnomalidad.objects.all().order_by('-timestamp')
    serializer_class = EventoAnomalidadSerializer
    permission_classes = [IsAuthenticated]

class EstadisticaDiariaViewSet(viewsets.ModelViewSet):
    #
    #ViewSet para consultar las estadísticas diarias.
    #
    queryset = EstadisticaDiaria.objects.all().order_by('-fecha')
    serializer_class = EstadisticaDiariaSerializer
    permission_classes = [IsAuthenticated]

# Las vistas personalizadas como 'dashboard_general' o 'estadisticas_periodo'
# pueden requerir lógica más compleja que un simple CRUD, por lo que se
# mantienen como APIView por ahora.

from rest_framework.views import APIView

class DashboardGeneralView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Lógica para obtener el dashboard general
        return Response({"message": "Dashboard general obtenido exitosamente"}, status=status.HTTP_200_OK)

class EstadisticasPeriodoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Lógica para obtener estadísticas por período
        return Response({"message": "Estadísticas por período obtenidas exitosamente"}, status=status.HTTP_200_OK)
