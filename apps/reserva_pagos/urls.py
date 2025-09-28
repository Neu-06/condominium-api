from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('avisos', AvisoViewSet, basename='avisos')
router.register('reservas', ReservaViewSet, basename='reservas')
router.register('visitas', VisitaViewSet, basename='visitas')
router.register('conceptos-pago', ConceptoPagoViewSet, basename='conceptos-pago')
router.register('facturas', FacturaViewSet, basename='facturas')
router.register('detalles-factura', DetalleFacturaViewSet, basename='detalles-factura')
router.register('pagos', PagoViewSet, basename='pagos')
urlpatterns = [
    path('', include(router.urls)),
]