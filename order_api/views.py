
from.serializers import OrderHistorysCartSerializer,OrderListSerializer,CartCreateSerializer,CarUpdatetSerializer,OrderSerializer,OrderDetailsSerializer,OrderHistorysSerializer,OrderCreatesSerializer,CartSerializer
# ,OrderInvoicesSerializer,CarUpdatetSerializer,

from rest_framework import generics
from .models import Order,Cart
# 
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404
from dj_rest_auth.registration.serializers import (
    SocialAccountSerializer, SocialConnectSerializer, SocialLoginSerializer
  )
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class OrderListApiView(generics.ListAPIView):
    """for getting one item inside the cart"""
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    lookup_field = 'cart'
  
    
    

class OrderDeleteApiView(generics.DestroyAPIView):
    """for deleteing one item inside the cart"""
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
  
    
class OrderUpdateApiView(generics.UpdateAPIView):
    """for updating  one item inside the cart (qnt)"""
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    


 
class OrderDetailsListApiView(generics.ListAPIView):
    
    serializer_class=OrderDetailsSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'cart'
    
    
    
    

class OrderHistorysApiView(generics.ListAPIView):
    # queryset=Order.objects.all()
    serializer_class=OrderHistorysCartSerializer
    lookup_field = 'user'
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        id =self.kwargs.get(self.lookup_field)

    # Here you can do the following thing:
    

    # And use it as you wish in the filtering below:

        return Cart.objects.filter(user=id)
        
    # current_user = self.request.user.id
    # print(current_user)
    
    
    
    
class OrderCreatesApiView(generics.CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderCreatesSerializer
  
    # permission_classes = [IsAuthenticated]
    
class CartCreatesApiView(generics.CreateAPIView):
    """ for creating the cart with item and user"""
    queryset=Cart.objects.all()
    serializer_class=CartCreateSerializer
   



class CartDeleteesApiView(generics.DestroyAPIView):
    """ for deleteing the cart"""
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    lookup_field = 'pk'


class CartListApiView(generics.ListAPIView):
    """ for retreiving the cart for specific user with all items inside it """
    
    serializer_class=CartSerializer
    lookup_field = 'user'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return Cart.objects.filter(user=id)
    # permission_classes = [IsAuthenticated]
    
class CartUpdateApiView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CarUpdatetSerializer
    lookup_field = 'pk'

   
            
    
        
class OrderListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    serializer_class =OrderListSerializer
        
        
        
        
        
