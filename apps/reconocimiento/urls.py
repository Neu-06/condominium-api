from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'rostros', RostroResidenteViewSet, basename='rostro')
router.register(r'historial-accesos', RegistroAccesoFacialViewSet, basename='historial-acceso')

urlpatterns = [
    path('', include(router.urls)),
    path('verificar_rostro/', VerificarRostroView.as_view(), name='verificar_rostro'),
    path('reconocimiento_facial/', ReconocimientoFacialView.as_view(), name='reconocimiento_facial'),
    path('registrar_rostro/', RegistrarRostroView.as_view(), name='registrar_rostro'),
    path('reconocimiento_placa/', ReconocimientoPlacaView.as_view(), name='reconocimiento_placa'),
]
