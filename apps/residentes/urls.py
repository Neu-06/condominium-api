from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResidenteViewSet

router = DefaultRouter()
router.register('residentes', ResidenteViewSet, basename='residentes')

urlpatterns = [
    path('', include(router.urls)),
]