from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']


class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra):
        if not correo:
            raise ValueError('El correo es obligatorio')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra)
        if password:
            user.set_password(password)  # hash
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, correo, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_active', True)
        if extra.get('is_staff') is not True:
            raise ValueError('Superusuario requiere is_staff=True')
        if extra.get('is_superuser') is not True:
            raise ValueError('Superusuario requiere is_superuser=True')
        return self.create_user(correo, password, **extra)


class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')

    # Campos obligatorios para integración Django Admin / auth
    is_active = models.BooleanField(default=True)      
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []  
    objects = UsuarioManager()

    def __str__(self):
        return self.correo

    class Meta:
        db_table = 'usuario'
        ordering = ['correo']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'