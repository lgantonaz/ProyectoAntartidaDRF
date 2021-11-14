from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AntartidaFront.urls', namespace='AntartidaFront')),
    path('api/', include('AntartidaAPI.urls', namespace='AntartidaAPI')),

]
