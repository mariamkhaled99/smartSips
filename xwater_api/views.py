from django.shortcuts import render
from rest_framework import generics
from xwater.models import Product
from .serializers import ProducttSerializer


# we can list and create items by this view 
class ProductList(generics.ListCreateAPIView):
    queryset=Product.productobjects.all()
    serializer_class=ProducttSerializer


# we can retrive and delete specific item by this view 
class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer
