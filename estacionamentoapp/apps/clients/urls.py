from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'clients'

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='client')

# Definindo a URL
urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as URLs do router
]
