from django.db import models

class Sensor(models.Model):
    # idSensor=models.AutoField(primary_key= True)
    nombre=models.CharField(max_length=30)
    latitud=models.BigIntegerField
    longitud=models.BigIntegerField