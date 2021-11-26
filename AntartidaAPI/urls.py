from django.urls import path
from .views import *

app_name = 'AntartidaAPI'

urlpatterns = [

    # URLS DE LOS SENSORES
    path('sensor/detail/<int:pk>/', sensor_detail_view, name='sensor_detail_view'),
    # path('sensor/update/<int:pk>/', SensorDetail.as_view(), name='detailCreate'),
    path('sensor/', sensor_view, name='list'),
    #path('sensor/getall', SensorList.as_view(), name='list'),
    # path('sensor/create', SensorCreate.as_view(), name='create'),
    path('sensor/create', sensor_view, name='create'),

    #URLS DE LAS LECTURA
    #path('lectura/', lectura_view, name='list'),

    # URLS DE LOS USUARIOS
    path('usuario/', usuario_view, name='list'),
    path('usuario/detail/<int:pk>/', usuario_detail_view, name='usuario_detail_view'),

    # URLS DEl ROL
    # path('rol/', RolList.as_view(), name='listCreate'),

]
