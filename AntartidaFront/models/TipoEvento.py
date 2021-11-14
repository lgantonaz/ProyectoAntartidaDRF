from django.db import models

class TipoEvento(models.Model):
    # solo tiene nombre porque es para identificarlo si en un futuro se agregan mas eventos creables por el usuario
    nombre=models.CharField(max_length=30)