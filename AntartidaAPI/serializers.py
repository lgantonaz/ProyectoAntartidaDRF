from django.db.models import fields
from rest_framework import serializers
from AntartidaFront.models import *


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('nombre_sensor','latitud','longitud')
    
# class SensorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ('id', 'nombreSensor', 'latitud', 'longitud')
        
# class SensorUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ('nombreSensor', 'latitud', 'longitud', 'deleted')

# class SensorListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ('id', 'nombreSensor', 'latitud', 'longitud') 
        
# class SensorCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ('nombreSensor', 'latitud', 'longitud') 

#     def validate_latitud(self, value):
#         if 0 == value:
#             raise serializers.ValidationError("La latitud no puede ser igual 0")
#         return value
    
#     def validate_longitud(self, value):
#         if 0 == value:
#             raise serializers.ValidationError("La longitud no puede ser igual 0")
#         return value
    
#     def create(self, validated_data):
#         return super().create(validated_data)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'rol')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')