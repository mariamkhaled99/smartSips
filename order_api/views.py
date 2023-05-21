
from.serializers import OrderSerializer,OrderDetailsSerializer,OrderHistorysSerializer,OrderCreatesSerializer,CartSerializer
# ,OrderInvoicesSerializer

from rest_framework import generics
from .models import Order,Cart
# 
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404
from dj_rest_auth.registration.serializers import (
    SocialAccountSerializer, SocialConnectSerializer, SocialLoginSerializer
  )

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
    
class CartCreatesApiView(generics.CreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    # permission_classes = [IsAuthenticated]


class CartListApiView(generics.ListAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    lookup_field = 'user'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return Cart.objects.filter(id=id)
    # permission_classes = [IsAuthenticated]
    
class CartUpdateApiView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CartSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "cart updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})