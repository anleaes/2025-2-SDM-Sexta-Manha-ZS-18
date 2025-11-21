from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orderitems'

router = routers.DefaultRouter()
router.register('', views.OrderitemViewSet, basename='itens_pedido')

urlpatterns = [
    path('', include(router.urls) )
]