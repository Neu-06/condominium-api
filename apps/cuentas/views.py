from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .models import Usuario, Rol
from .serializers import (
    UsuarioReadSerializer,
    UsuarioWriteSerializer,
    RolSerializer,
    RegistroSerializer,
    PerfilSerializer
)

# LOGIN usando correo + password => devuelve access / refresh y usuario
class LoginJWTView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')
        user = authenticate(request, correo=correo, password=password)
        if not user:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({'detail': 'Usuario inactivo'}, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'usuario': UsuarioReadSerializer(user).data
        })

# PERFIL (requiere Bearer token)
class PerfilView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ser = PerfilSerializer(request.user)
        return Response(ser.data)

# ROLES CRUD
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().order_by('id')
    serializer_class = RolSerializer

# USUARIOS CRUD
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().select_related('rol').order_by('id')

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return UsuarioWriteSerializer
        return UsuarioReadSerializer

class LogoutJWTView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Falta refresh'}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # requiere app blacklist
        except Exception:
            return Response({'detail': 'Refresh inválido'}, status=400)
        return Response({'detail': 'OK'})

class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ser = RegistroSerializer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            return Response({'id': user.id, 'correo': user.correo}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)