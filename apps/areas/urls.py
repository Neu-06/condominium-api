from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AreaComunViewSet, ReglaViewSet

router = DefaultRouter()
router.register('areas-comunes', AreaComunViewSet, basename='areas-comunes')
router.register('reglas', ReglaViewSet, basename='reglas')

urlpatterns = [
    path('', include(router.urls)),
]