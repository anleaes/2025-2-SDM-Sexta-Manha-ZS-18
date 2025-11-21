from django.shortcuts import render
from .models import Client, Veiculo, EnderecoCliente
from rest_framework import viewsets
from .serializer import ClientSerializer , VeiculoSerializer, EnderecoClienteSerializer
# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class EnderecoClienteViewSet(viewsets.ModelViewSet):
    queryset = EnderecoCliente.objects.all()
    serializer_class = EnderecoClienteSerializer