from rest_framework import response,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from AntartidaFront.models import *
from .serializers import *
import logging
import json
# Utilizando los genericos de DRF crea automaticamente los controllers(llamados views en django)

logger = logging.getLogger(__name__)
@api_view(['GET', 'POST'])
def sensor_view(request):
    if(request.method == 'GET'):
        sensores = Sensor.sensores_objects.all()
        sensores_serializer = SensorSerializer(sensores, many=True)
        return Response(sensores_serializer.data)

    elif(request.method == 'POST'):
        if (request.POST.get('nombre_sensor')): 
            try:   
                sensor = Sensor.objects.get(nombre=request.POST.get('nombre_sensor'))
            except:
                sensor = Sensor.objects.create(nombre=request.POST.get('nombre_sensor'))
            lectura = Lectura.objects.create(sensor_id = sensor.id, fecha_lectura = request.POST.get('fecha_lectura'))
            mediciones= json.loads(request.POST.get('lectura'))
            
            for medicion in mediciones:
                try:
                    tipo_medicion = TipoMedicion.objects.get(nombre=medicion['tipo'])
                    medicion = Medicion.objects.create(lectura_id = lectura.id, tipo_medicion_id=tipo_medicion.id,valor=int(medicion['valor']))
                except:
                    print('OMAR ALGO ANDA MAL')
            return Response({}, status=status.HTTP_201_CREATED)


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
