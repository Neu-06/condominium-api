from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PrediccionMorosidadViewSet,
    EventoAnomalidadViewSet,
    EstadisticaDiariaViewSet,
    DashboardGeneralView,
    EstadisticasPeriodoView,
)

router = DefaultRouter()
router.register(r'predicciones-morosidad', PrediccionMorosidadViewSet, basename='prediccion-morosidad')
router.register(r'eventos-anomalos', EventoAnomalidadViewSet, basename='evento-anomalo')
router.register(r'estadisticas-diarias', EstadisticaDiariaViewSet, basename='estadistica-diaria')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard_general/', DashboardGeneralView.as_view(), name='dashboard_general'),
    path('estadisticas_periodo/', EstadisticasPeriodoView.as_view(), name='estadisticas_periodo'),
]
