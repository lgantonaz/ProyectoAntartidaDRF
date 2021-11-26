from django.urls import path
from .views import *

app_name = 'AntartidaAPI'

urlpatterns = [

    # URLS DE LOS SENSORES
    path('sensor/', sensor_view, name='list'),
    path('sensor/detail/<int:id>/', sensor_detail_view, name='sensor_detail_view'),
    path('sensor/create', sensor_view, name='create'),
    # path('sensor/update/<int:id>/', SensorDetail.as_view(), name='detailCreate'),
    #path('sensor/getall', SensorList.as_view(), name='list'),
    # path('sensor/create', SensorCreate.as_view(), name='create'),
    

    #URLS DE LAS LECTURA
    path('lectura/', lectura_view, name='list'),
    path('lectura/detail/<int:id>/', lectura_detail_view, name='lectura_detail_view'),
    path('lectura/create', lectura_view, name='create'),
    
    #URLS DE LAS MEDICION
    path('medicion/', medicion_view, name='list'),
    path('medicion/detail/<int:id>/', medicion_detail_view, name='medicion_detail_view'),
    path('medicion/create', medicion_view, name='create'),

    # URLS DE LOS USUARIOS
    path('usuario/', usuario_view, name='list'),
    path('usuario/detail/<int:id>/', usuario_detail_view, name='usuario_detail_view'),
    path('usuario/create', usuario_view, name='create'),

    # URLS DEl ROL
    # path('rol/', RolList.as_view(), name='listCreate'),

]
