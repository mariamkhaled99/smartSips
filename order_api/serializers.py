from rest_framework import serializers
from .models import Order
from user_api.models import CustomUser,UserProfile,AdminProfile
from products_api.models import Product

                
class OrderSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    address=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()
    
    class Meta:
        model=Order
        fields=('id','amount','total_price','items','order_date','address','username')
        # read_only_fields = (,)
        
        def amount(self):
            amount=Order.items.count()
            return amount
    
        def total_price(self):
            for item in Order.items:
                total_price=0
                total_price=item['price']+total_price
            return total_price
        def address(self):
            address=UserProfile.address
            return address
        
        def username(self):
            username=CustomUser.username
            return username


class OrderDetailsSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields=('id','amount','total_price','delivery_date','order_date')
        # read_only_fields = (,)
        
        def amount(self):
            amount=Order.items.count()
            return amount
    
        def total_price(self):
            for item in Order.items:
                total_price=0
                total_price=item['price']+total_price
            return total_price
        
        
class OrderInvoicesSerializer(serializers.ModelSerializer):
    qty=serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields=('id','amount','total_price','delivery_date','order_date')
        
        
class OrderInvoicesSerializer(serializers.ModelSerializer):
    company=serializers.SerializerMethodField()
    category=serializers.SerializerMethodField()
    image=serializers.SerializerMethodField()
    
    
    class Meta:
        model=Order
        fields=('id','company','category','image','delivery_date')
        def company(self):
            company=AdminProfile.company
            return company
        def category(self):
            category=Product.category
            return category
        def category(self):
            image=Product.image
            return image
        
    
        
    
        
        
        
        
       


    