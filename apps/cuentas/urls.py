from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginJWTView, PerfilView, RolViewSet, UsuarioViewSet, RegistroView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('roles', RolViewSet, basename='roles')
router.register('usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('token/', LoginJWTView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('', include(router.urls)),
]
