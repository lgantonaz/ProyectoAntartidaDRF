from django.urls import path
from .views import *

app_name = 'AntartidaAPI'

urlpatterns = [

    # URLS DE LOS SENSORES
    path('<int:pk>/', SensorDetail.as_view(), name='detailCreate'),
    path('sensor/', SensorList.as_view(), name='listCreate'),

    # URLS DE LOS USUARIOS
    path('usuario/', UsuarioList.as_view(), name='listCreate'),

    # URLS DEl ROL
    path('rol/', RolList.as_view(), name='listCreate'),

]
