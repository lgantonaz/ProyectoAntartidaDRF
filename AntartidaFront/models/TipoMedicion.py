from django.db import models


class TipoMedicion(models.Model):
    # idTipoMedicion=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    unidad=models.CharField(max_length=30)