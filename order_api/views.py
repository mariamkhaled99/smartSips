
from.serializers import OrderInvoiceCreateSerializer,PaymentSerializer,YearModelSerializer,MonthModelSerializer,LocationModelSerializer,OrderHistorysCartSerializer,OrderListSerializer,CartCreateSerializer,CarUpdatetSerializer,OrderSerializer,OrderDetailsSerializer,OrderHistorysSerializer,OrderCreatesSerializer,CartSerializer
# ,OrderInvoicesSerializer,CarUpdatetSerializer,
# 
from rest_framework import generics
from .models import Order,Cart,LocationModel,MonthModel,YearModel,payment,OrderInvoice
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

   
            
    
        
class OrderListAllAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    serializer_class =OrderListSerializer
        
        
        
        
        
    
class YearModelCreatesApiView(generics.CreateAPIView):
    queryset=YearModel.objects.all()
    serializer_class=YearModelSerializer


    
class MonthModelApiView(generics.CreateAPIView):
    queryset=MonthModel.objects.all()
    serializer_class=MonthModelSerializer
    
    
    
    
class LocationApiView(generics.CreateAPIView):
    queryset=LocationModel.objects.all()
    serializer_class=LocationModelSerializer
    
class OrderInvoiceCreateAPIVIEW(generics.CreateAPIView):
    queryset=OrderInvoice.objects.all()
    serializer_class=OrderInvoiceCreateSerializer

    
class PaymentApiView(generics.CreateAPIView):
    queryset=payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        # custom logic here
        billingaddress = request.data.get('billingaddress')
        city = request.data.get('city')
        fullname = request.data.get('fullname')
        zipcode = request.data.get('zipcode')
        country_id = request.data.get('country')
        month_id = request.data.get('month')
        year_id=request.data.get('year')
        cardholdername = request.data.get('cardholdername')
        cvv = request.data.get('cvv')
        cardnumber = request.data.get('cardnumber')

        # create a new LocationModel instance
        country = LocationModel.objects.get(pk=country_id)
        month = MonthModel.objects.get(pk=month_id)
        year = YearModel.objects.get(pk=year_id)

        payment.objects.create(
            cardnumber=cardnumber,
            cvv=cvv,
            billingaddress=billingaddress,
            city=city,
            fullname=fullname,
            zipcode=zipcode,
            country=country,
            month=month,
            year=year,
            cardholdername=cardholdername
        )
        # OrderInvoice.objects.create()
        # # Cart.objects.filter(user=id)
        return Response({'is_paied': True}, status=200)
   
        