from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

