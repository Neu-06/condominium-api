from rest_framework import serializers
from .models import Usuario, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

class UsuarioReadSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre', 'apellido', 'telefono', 'is_active', 'last_login', 'rol']

class UsuarioWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        source='rol', queryset=Rol.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'password', 'nombre', 'apellido', 'telefono', 'rol_id', 'is_active']

    def to_internal_value(self, data):
        # Permitir actualizar sin password en PUT/PATCH
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
        fields = ['id', 'correo', 'password', 'nombre', 'apellido']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

class PerfilSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(source='rol.nombre', read_only=True)  # ajusta según tu modelo (rol.nombre o rol.slug)

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre', 'apellido', 'rol']

