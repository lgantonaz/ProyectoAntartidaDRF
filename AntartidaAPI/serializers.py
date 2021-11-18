from django.db.models import fields
from rest_framework import serializers
from AntartidaFront.models import *


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('__all__')

class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'nombreSensor', 'latitud', 'longitud')

class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'nombreSensor', 'latitud', 'longitud') 


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'rol')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')