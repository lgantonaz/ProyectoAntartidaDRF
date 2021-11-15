from rest_framework import serializers
from AntartidaFront.models import *


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('nombreSensor', 'latitud', 'longitud', 'deleted')
