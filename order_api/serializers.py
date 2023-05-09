from rest_framework import serializers
from .models import Order
from user_api.models import CustomUser
from products_api.models import Product
# ,UserProfile,AdminProfile
                
class OrderSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    total_price = serializers.IntegerField()
    address=serializers.CharField()
    username=serializers.CharField()
    
    class Meta:
        model=Order
        fields=('id','amount','total_price','items','order_date','address','username')
        # read_only_fields = (,)
        
        


class OrderDetailsSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    total_price = serializers.IntegerField()
    class Meta:
        model=Order
        fields=('id','amount','total_price','delivery_date','order_date')
        # read_only_fields = (,)
        
       
        
        
# class OrderInvoicesSerializer(serializers.ModelSerializer):
#     qty=serializers.SerializerMethodField()
#     class Meta:
#         model=Order
#         fields=('id','amount','total_price','delivery_date','order_date')
        
        
class OrderHistorysSerializer(serializers.ModelSerializer):
    company=serializers.CharField()
    category=serializers.PrimaryKeyRelatedField(read_only='True')
    image=serializers.ImageField()
    
    
    class Meta:
        model=Order
        fields=('id','company','category','image','delivery_date')
        
class OrderCreatesSerializer(serializers.ModelSerializer):
     class Meta:
        model=Order
        fields=('id','items','user')
      
    
        
    
        
        
        
        
       


    