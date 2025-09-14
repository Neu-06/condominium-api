from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Residente
from .serializers import ResidenteSerializer

class ResidenteViewSet(viewsets.ModelViewSet):
    queryset = Residente.objects.all().order_by('id')
    serializer_class = ResidenteSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
