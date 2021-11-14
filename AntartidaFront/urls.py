from django.urls import path
from django.views.generic import TemplateView


app_name = 'AntartidaFront'

urlpatterns = [
    path('', TemplateView.as_view(template_name='AntartidaFront/index.html')),
]
