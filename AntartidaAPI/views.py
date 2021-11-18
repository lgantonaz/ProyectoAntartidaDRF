from rest_framework import generics
from AntartidaFront.models import *
from .serializers import *

# Utilizando los genericos de DRF crea automaticamente los controllers(llamados views en django)


class SensorListCreate(generics.ListCreateAPIView):
    queryset = Sensor.sensoresObjects.all() #estoy usando el custom manager que cree, que me devuelve solo los sensores que tienen deleted=false
    serializer_class = SensorSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.usuariosObjects.all() #estoy usando el custom manager que cree, que me devuelve solo los sensores que tienen deleted=false
    serializer_class = UsuarioSerializer



class RolList(generics.ListCreateAPIView):
    queryset = Rol.objects.all() #estoy usando el custom manager que cree, que me devuelve solo los sensores que tienen deleted=false
    serializer_class = RolSerializer


class SensorDetail(generics.RetrieveDestroyAPIView):
    queryset  = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    
class SensorList(generics.ListAPIView):
    queryset  = Sensor.objects.all()
    serializer_class = SensorListSerializer

class SensorCreate(generics.CreateAPIView):
    queryset  = Sensor.objects.all()
    serializer_class = SensorCreateSerializer




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