from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from apps.residentes.models import Residente
from .models import logReconocimiento
from .serializers import LogReconocimientoSerializer
from decouple import config
import requests

class ReconocimientoFacialView(APIView):
    def post(self, request):
        try:
            url_foto = request.data.get('foto_url')
            if not url_foto:
                return Response({'error': 'No se envió la foto'}, status=status.HTTP_400_BAD_REQUEST)
            
            residentes = Residente.objects.all()
            mejor_coincidencia = 0
            residente_encontrado = None
            confianza_umbral = 70

            for residente in residentes:
                try:
                    url_foto_residente = getattr(residente, 'foto_perfil', None)
                    if not url_foto_residente:
                        continue

                    api_key = config('FACEPP_API_KEY')
                    api_secret = config('FACEPP_API_SECRET')
                    url = "https://api-us.faceplusplus.com/facepp/v3/compare"
                    data = {
                        "api_key": api_key,
                        "api_secret": api_secret,
                        "image_url1": url_foto,
                        "image_url2": url_foto_residente
                    }
                    resp = requests.post(url, data=data)
                    result = resp.json()
                    confidence = result.get('confidence', 0)
                    if confidence > mejor_coincidencia:
                        mejor_coincidencia = confidence
                        residente_encontrado = residente
                    if mejor_coincidencia >= confianza_umbral:
                        break
                except Exception as e:
                    continue

            # Crear log
            try:
                if residente_encontrado and mejor_coincidencia >= confianza_umbral:
                    log = logReconocimiento.objects.create(
                        residente=residente_encontrado,
                        foto_ruta=url_foto,
                        descripcion="Reconocimiento facial exitoso",
                        coincidencia=float(mejor_coincidencia)
                    )
                    return Response({
                        'autorizado': True,
                        'residente': {
                            'id': residente_encontrado.id,
                            'nombre': getattr(residente_encontrado, 'nombre', '') or '',
                            'apellido': getattr(residente_encontrado, 'apellido', '') or '',
                            'foto_perfil': getattr(residente_encontrado, 'foto_perfil', '') or '',
                        },
                        'coincidencia': float(mejor_coincidencia)
                    }, status=status.HTTP_200_OK)
                else:
                    log = logReconocimiento.objects.create(
                        residente=None,
                        foto_ruta=url_foto,
                        descripcion="No pertenece al residencial",
                        coincidencia=float(mejor_coincidencia)
                    )
                    return Response({
                        'autorizado': False,
                        'mensaje': 'No se encontró coincidencia suficiente',
                        'coincidencia': float(mejor_coincidencia)
                    }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    'error': f'Error al guardar log: {str(e)}',
                    'autorizado': False,
                    'coincidencia': float(mejor_coincidencia)
                }, status=status.HTTP_200_OK)
                
        except Exception as e:
            return Response({
                'error': f'Error interno del servidor: {str(e)}',
                'autorizado': False,
                'coincidencia': 0.0
            }, status=status.HTTP_200_OK)

class LogReconocimientoListView(generics.ListAPIView):
    serializer_class = LogReconocimientoSerializer
    
    def get_queryset(self):
        try:
            return logReconocimiento.objects.all().order_by('-fecha_hora')
        except Exception as e:
            return logReconocimiento.objects.none()
    
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
