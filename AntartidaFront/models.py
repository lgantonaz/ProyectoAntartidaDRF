from django.db import models
from django.db.models import query


class Rol(models.Model):
    nombreRol = models.CharField(max_length=30)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreRol


class Sensor(models.Model):

    # esto lo que hace retornar por defecto solo los sensores que tienen deleted=false
    # en lugar de hacer Objects.all() cuando hacemos la query, hacemos SensoresObjects y devuelve solo los que no estan borrados
    class SensoresObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(deleted=False)

    # idSensor=models.AutoField(primary_key= True)
    nombreSensor = models.CharField(max_length=30)
    latitud = models.BigIntegerField
    longitud = models.BigIntegerField
    deleted = models.BooleanField(default=False)
    objects = models.Manager()  # default model manager
    sensoresObjects = SensoresObjects()  # custom manager

    def __str__(self):
        return self.nombreSensor


class TipoEvento(models.Model):
    # solo tiene nombre porque es para identificarlo si en un futuro se agregan mas eventos creables por el usuario
    nombre = models.CharField(max_length=30)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class TipoMedicion(models.Model):
    # idTipoMedicion=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    unidadDeMedida = models.CharField(max_length=30)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + 'unidad:' + self.unidadDeMedida


class Usuario(models.Model):
    # idUsuario=models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + self.apellido + 'email: ' + self.email


class Evento(models.Model):
    tituloEvento = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    usuario = models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.CASCADE)
    sensor = models.ForeignKey(
        Sensor, null=True, blank=True, on_delete=models.CASCADE)
    fechaEvento = models.DateTimeField(auto_now_add=False)
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.tituloEvento

    class Meta:
        ordering = ('-fechaEvento',)


class Lectura(models.Model):
    # idLectura=models.AutoField(primary_key=True)
    # esta es la clave foranea al sensor
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    fechaLectura = models.DateTimeField(auto_now_add=False)
    # este campo es por si quiere agregarle alguna informacion relacionada a la lectura (por ej. midio 200 grados porque....)
    infoAdicional = models.CharField(max_length=300, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.sensor + self.fechaLectura

    class Meta:
        ordering = ('-fechaLectura',)


class Medicion(models.Model):
    # idMedicion=models.AutoField(primary_key=True)
    # esta es la clave foranea al sensor
    lectura = models.ForeignKey(Lectura, on_delete=models.CASCADE)
    # esta es la clave foranea a la lectura
    tipoMedicion = models.ForeignKey(TipoMedicion, on_delete=models.PROTECT)
    # on_delete=models.CASCADE
    # tiene un largo de 300 caracteres porque si es una imagen le vamos a pasar el path
    valor = models.CharField(max_length=300)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.tipoMedicion + self.valor
