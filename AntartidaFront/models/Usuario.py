from django.db import models

from .Rol import Rol

class Usuario(models.Model):
    # idUsuario=models.AutoField(primary_key= True)
    nombre=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    rol=models.ForeignKey(Rol)