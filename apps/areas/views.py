from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AreaComun, Regla
from .serializers import AreaComunSerializer, ReglaSerializer

class AreaComunViewSet(viewsets.ModelViewSet):
    queryset = AreaComun.objects.all().order_by('id')
    serializer_class = AreaComunSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='asignar-reglas')
    def asignar_reglas(self, request, pk=None):
        area = self.get_object()
        reglas_ids = request.data.get('reglas', [])
        if not isinstance(reglas_ids, list):
            return Response({'detail': 'Formato inválido. Debe ser lista.'},
                            status=status.HTTP_400_BAD_REQUEST)
        reglas = Regla.objects.filter(id__in=reglas_ids)
        area.reglas.set(reglas)
        area.save()
        return Response({'detail': 'Reglas asignadas', 'reglas': [r.id for r in reglas]})

class ReglaViewSet(viewsets.ModelViewSet):
    queryset = Regla.objects.all().order_by('id')
    serializer_class = ReglaSerializer
    permission_classes = [IsAuthenticated]
