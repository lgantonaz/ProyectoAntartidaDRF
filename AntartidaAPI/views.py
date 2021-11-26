from rest_framework import response,status,generics
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

@api_view(['GET', 'PUT'])
def sensor_detail_view(request,pk=None):

    if request.method == 'GET':
        sensor = Sensor.sensores_objects.filter(id=pk).first()
        sensor_serializer = SensorSerializer(sensor)
        return Response(sensor_serializer.data)

    elif request.method == 'PUT':
        sensor = Sensor.sensores_objects.filter(pk=pk).first()
        sensor_serializer = SensorSerializer(sensor, data=request.data)
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            return Response(sensor_serializer.data)
        return Response(sensor_serializer.error_messages)

# def lectura_view(request):
#     if(request.method == 'GET'):
#         lecturas = Lectura.lecturas_objects.all()
#         lecturas_serializer = LecturaSerializer(lecturas, many=True)
#         return Response(lecturas_serializer.data)

@api_view(['GET'])
def usuario_view(request):
    if(request.method == 'GET'):
        usuarios = Usuario.usuarios_objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuarios_serializer.data)

@api_view(['GET', 'PUT'])
def usuario_detail_view(request,pk=None):

    if request.method == 'GET':
        usuario = Usuario.objects.filter(id=pk).first()
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)

    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(pk=pk).first()
        usuario_serializer = UsuarioSerializer(usuario, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.error_messages)

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
