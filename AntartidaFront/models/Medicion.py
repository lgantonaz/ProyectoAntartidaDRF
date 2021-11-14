from django.db import models

from .Lectura import Lectura
from .TipoMedicion import TipoMedicion


class Medicion(models.Model):
    # idMedicion=models.AutoField(primary_key=True)
    # esta es la clave foranea al sensor
    lectura=models.ForeignKey(Lectura, on_delete=models.CASCADE) 
    # esta es la clave foranea a la lectura
    tipoMedicion=models.ForeignKey(TipoMedicion) 
    # on_delete=models.CASCADE
    # tiene un largo de 300 caracteres porque si es una imagen le vamos a pasar el path
    valor=models.CharField(max_length=300)