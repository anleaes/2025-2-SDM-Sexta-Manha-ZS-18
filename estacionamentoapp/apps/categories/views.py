from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  