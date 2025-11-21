from .models import Orderitem
from rest_framework import serializers
    
class OrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderitem
        fields = '__all__'