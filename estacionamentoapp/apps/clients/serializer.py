from .models import Client, Veiculo, EnderecoCliente
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['Client_id', 'cpf', 'idade', 'ativo', 'first_name', 'last_name', 'address', 'cell_phone', 'email', 'gender', 'socialnetwork']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['veiculo_id', 'marca', 'modelo', 'placa', 'cor', 'cliente']

class EnderecoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoCliente
        fields = ['endereco_id', 'rua', 'bairro', 'numero', 'complemento', 'cliente']