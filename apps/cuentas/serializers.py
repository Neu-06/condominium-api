from rest_framework import serializers
from .models import Usuario, Rol, Bitacora, Aviso
from apps.residentes.models import Residente
from apps.personal.models import Personal

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

class UsuarioReadSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    residente_nombre = serializers.CharField(source='residente.nombre', read_only=True)
    personal_nombre = serializers.CharField(source='personal.nombre', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre', 'apellido', 'telefono', 'is_active', 'last_login', 
                 'rol', 'residente', 'residente_nombre', 'personal', 'personal_nombre']

class UsuarioWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        source='rol', queryset=Rol.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'password', 'nombre', 'apellido', 'telefono', 
                 'residente', 'personal', 'rol_id', 'is_active']

    def to_internal_value(self, data):
        if self.instance and 'password' not in data:
            self.fields['password'].required = False
        return super().to_internal_value(data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'password', 'nombre', 'apellido', 'residente', 'personal']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

class PerfilSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(source='rol.nombre', read_only=True)
    residente_info = serializers.SerializerMethodField()
    personal_info = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre', 'apellido', 'rol', 'residente_info', 'personal_info']

    def get_residente_info(self, obj):
        if obj.residente:
            return {
                'id': obj.residente.id,
                'nombre': obj.residente.nombre,
                'apellidos': obj.residente.apellidos,
                'residencia': obj.residente.residencia.numero if obj.residente.residencia else None
            }
        return None

    def get_personal_info(self, obj):
        if obj.personal:
            return {
                'id': obj.personal.id,
                'nombre': obj.personal.nombre,
                'cargo': obj.personal.cargo,
                'area': obj.personal.area.nombre if obj.personal.area else None
            }
        return None

class RecuperarPasswordSerializer(serializers.Serializer):
    correo = serializers.EmailField()

class CambiarPasswordSerializer(serializers.Serializer):
    password_actual = serializers.CharField()
    password_nueva = serializers.CharField(min_length=4)

class BitacoraSerializer(serializers.ModelSerializer):
    usuario_correo = serializers.CharField(source='usuario.correo', read_only=True)

    class Meta:
        model = Bitacora
        fields = ['id', 'usuario', 'usuario_correo', 'accion', 'descripcion', 'ip', 'fecha']
        read_only_fields = ['fecha']

class SolicitarRecuperacionSerializer(serializers.Serializer):
    correo = serializers.EmailField()

class ConfirmarRecuperacionSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    nueva_password = serializers.CharField(min_length=6, max_length=128)
    confirmar_password = serializers.CharField(max_length=128)
    
    def validate(self, attrs):
        if attrs['nueva_password'] != attrs['confirmar_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return attrs

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = ['id', 'asunto', 'mensaje', 'fecha_push', 'hora_push', 'urgente', 'estado']