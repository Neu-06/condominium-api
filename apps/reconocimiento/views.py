from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

class RostroResidenteViewSet(viewsets.ModelViewSet):
    #
    #ViewSet para gestionar los rostros de los residentes.
    #
    queryset = RostroResidente.objects.all()
    serializer_class = RostroResidenteSerializer
    permission_classes = [IsAuthenticated]

class RegistroAccesoFacialViewSet(viewsets.ModelViewSet):
    #
    #ViewSet para ver el historial de accesos faciales.
    #Principalmente para lectura (GET).
    #
    queryset = RegistroAccesoFacial.objects.all().order_by('-timestamp')
    serializer_class = RegistroAccesoFacialSerializer
    permission_classes = [IsAuthenticated]

# Las vistas personalizadas como 'verificar_rostro' se pueden mantener como APIView
# o añadirse como acciones personalizadas a un ViewSet si es necesario.
# Por ahora, las mantenemos simples y separadas.

class VerificarRostroView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Lógica para verificar el rostro
        return Response({"message": "Rostro verificado exitosamente"}, status=status.HTTP_200_OK)

class ReconocimientoFacialView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Lógica para el reconocimiento facial
        return Response({"message": "Reconocimiento facial exitoso"}, status=status.HTTP_200_OK)

class RegistrarRostroView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Lógica para registrar un nuevo rostro
        return Response({"message": "Rostro registrado exitosamente"}, status=status.HTTP_200_OK)

class ReconocimientoPlacaView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Lógica para el reconocimiento de placa
        return Response({"message": "Placa reconocida exitosamente"}, status=status.HTTP_200_OK)
