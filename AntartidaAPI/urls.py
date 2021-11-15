from django.urls import path
from .views import SensorList, SensorDetail


app_name = 'AntartidaAPI'

urlpatterns = [
    path('<int:pk>/', SensorDetail.as_view(), name='detailCreate'),
    path('', SensorList.as_view(), name='listCreate')
]
