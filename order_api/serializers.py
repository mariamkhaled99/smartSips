from rest_framework import serializers
from .models import Order,Cart
from user_api.models import CustomUser
from products_api.models import Product
from products_api.serializers import ProducttSerializer
# ,UserProfile,AdminProfile
                # ,Cart
class OrderSerializer(serializers.ModelSerializer):
    # amount = serializers.IntegerField()
    price = serializers.IntegerField(read_only=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Order
        fields=('id','price','item','qnt')
        # read_only_fields = (,)
        # ,'amount'
        
        


class OrderDetailsSerializer(serializers.ModelSerializer):
    # amount = serializers.IntegerField()
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    class Meta:
        model=Order
        fields=('id','qnt','price')
        # read_only_fields = (,)
        
       
        
        
# class OrderInvoicesSerializer(serializers.ModelSerializer):
#     qty=serializers.SerializerMethodField()
#     class Meta:
#         model=Order
#         fields=('id','amount','total_price','delivery_date','order_date')
        
        
class OrderHistorysSerializer(serializers.ModelSerializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    company=serializers.CharField(read_only=True)
    category=serializers.PrimaryKeyRelatedField(read_only=True)
    image=serializers.ImageField(read_only=True)
    
    
    class Meta:
        model=Order
        fields=('id','company','category','image')
        
class OrderCreatesSerializer(serializers.ModelSerializer):
    # items=ProducttSerializer(many=True, read_only=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    class Meta:
        model=Order
        fields=('id','item','qnt','price')
      
    # ,'amount'
      
    
class  CartSerializer(serializers.ModelSerializer):
    items = OrderSerializer(many=True, read_only=True)
    # items=ProducttSerializer(many=True, read_only=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    address=serializers.CharField(read_only=True)
    username=serializers.CharField(read_only=True)
    total_price=serializers.IntegerField(read_only=True)
    amount=serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'delivery_date','user', 'order_date','items','address','username','amount','total_price']


        
        
        
       


    