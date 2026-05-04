from django.db import models
from django.contrib.auth.models import User

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.usuario.username}/{filename}"

class Perfil (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_upload_to, default='avatars/default.png', null=True, blank=True)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.CharField(max_length=15, unique=True, null=True, blank=True)

def __str__(self):
    return f"{self.usuario.username} ({self.usuario.first_name} {self.usuario.last_name})"
