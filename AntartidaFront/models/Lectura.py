from django.db import models

from .Sensor import Sensor


class Lectura(models.Model):
    # idLectura=models.AutoField(primary_key=True)
    # esta es la clave foranea al sensor
    sensor=models.ForeignKey(Sensor, on_delete=models.CASCADE) 
    fechaLectura=models.DateTimeField(auto_now_add= False)
    # este campo es por si quiere agregarle alguna informacion relacionada a la lectura (por ej. midio 200 grados porque....)
    infoAdicional=models.CharField(max_length=300, null=True)