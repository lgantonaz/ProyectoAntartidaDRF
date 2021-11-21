from django.urls import path
from .views import *

app_name = 'AntartidaAPI'

urlpatterns = [

    # URLS DE LOS SENSORES
    path('sensor/detail/<int:pk>/', SensorDetail.as_view(), name='detailCreate'),
    path('sensor/update/<int:pk>/', SensorDetail.as_view(), name='detailCreate'),
    path('sensor/', SensorListCreate.as_view(), name='listCreate'),
    path('sensor/getall', SensorList.as_view(), name='list'),
    path('sensor/create', SensorCreate.as_view(), name='create'),

    # URLS DE LOS USUARIOS
    path('usuario/', UsuarioList.as_view(), name='listCreate'),

    # URLS DEl ROL
    path('rol/', RolList.as_view(), name='listCreate'),

]
