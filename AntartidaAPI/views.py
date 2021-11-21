from rest_framework.decorators import api_view
from rest_framework.response import Response
from AntartidaFront.models import *
from .serializers import *

# Utilizando los genericos de DRF crea automaticamente los controllers(llamados views en django)


@api_view(['GET', 'POST'])
def sensor_view(request):

    if(request.method == 'GET'):
        sensores = Sensor.sensores_objects.all()
        sensores_serializer = SensorSerializer(sensores, many=True)
        return Response(sensores_serializer.data)

    elif(request.method == 'POST'):
        sensor_serializer = SensorSerializer(data=request.data)
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            id_sensor = sensor_serializer.data.id
            
        # si esta creado, que busque ese sensor y me devuelva el id
        elif not sensor_serializer.is_valid():
            sensores = Sensor.objects.all()
            # buscar en todos los sensores el que coincida con el id que mando

    return Response(sensor_serializer.errors)


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
