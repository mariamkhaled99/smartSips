
from.serializers import OrderSerializer,OrderDetailsSerializer,OrderHistorysSerializer,OrderCreatesSerializer
# ,OrderInvoicesSerializer
from rest_framework import generics
from .models import Order

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404

class OrderListApiView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes = [IsAuthenticated]
    

class OrderDeleteApiView(generics.DestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


 
class OrderDetailsListApiView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderDetailsSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
    
    

class OrderHistorysApiView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderHistorysSerializer
    # permission_classes = [IsAuthenticated]
    
    
class OrderCreatesApiView(generics.CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderCreatesSerializer
    # permission_classes = [IsAuthenticated]
    

