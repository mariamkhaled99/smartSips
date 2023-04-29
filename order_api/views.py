
from.serializers import OrderSerializer,OrderDetailsSerializer
from rest_framework import generics
from .models import Order

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404

class OrderListSerializer(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes = [IsAuthenticated]
    

class OrderDeleteSerializer(generics.DestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


 
class OrderDetailsListSerializer(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderDetailsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    

