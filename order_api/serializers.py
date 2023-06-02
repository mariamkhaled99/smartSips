from rest_framework import serializers
from .models import Order,Cart
from user_api.models import CustomUser
from products_api.models import Product
from products_api.serializers import ProducttSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

        
        


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
    
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    class Meta:
        model=Order
        fields=('id','product','qnt','price','cart')
      
class YourcartProduct(serializers.ModelSerializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Product
        fields=('id','category','title','price','image')
       

class OrderSerializer(serializers.ModelSerializer):
    
    # product=YourcartProduct(read_only=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    priceqnt=serializers.SerializerMethodField(method_name="price_qnt")
    class Meta:
        model=Order
        fields=('id','product','qnt', 'priceqnt')
    def price_qnt(self,orderitem:Order):
        """for one item"""
    
        priceqnt=orderitem.product.price*orderitem.qnt
        return priceqnt

class OrderCartSerializer(serializers.ModelSerializer):
    """ to use this seializer with cart to create nested writable"""
    product=YourcartProduct()
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    priceqnt=serializers.SerializerMethodField(method_name="price_qnt")
    class Meta:
        model=Order
        fields=('id','product','qnt', 'priceqnt')
    def price_qnt(self,orderitem:Order):
        """for one item"""
    
        priceqnt=orderitem.product.price*orderitem.qnt
        return priceqnt
        
        
   


class CartSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    items = OrderCartSerializer( many=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    address=serializers.CharField(read_only=True)
    username=serializers.CharField(read_only=True)
    total_price=serializers.SerializerMethodField(method_name="total")
    amount=serializers.SerializerMethodField(method_name="amount_of_products")
    shipping=serializers.IntegerField(read_only=True)
    finalprice=serializers.SerializerMethodField(method_name="final_total_price")
 

    
    class Meta:
        model = Cart
        fields = ['id', 'delivery_date','user','items' ,'order_date','address','username','amount','total_price','shipping','finalprice']
            
    def amount_of_products(self,cartitems:Cart):
        """for all items"""
        amount=0
        for i in cartitems.items.all():
            amount=i.qnt+amount
        return amount
    def total(self,cartitems:Cart):
        """for one item"""
        total_price=0
        for i in cartitems.items.all():
            total_price=(i.product.price*i.qnt)+total_price
        return total_price
    def final_total_price(self,cartitems:Cart):
        total_price=0
        for i in cartitems.items.all():
            total_price=(i.product.price*i.qnt)+total_price
        finalprice=total_price+cartitems.shipping
        return finalprice
    
    
class CartCreateSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    items = OrderSerializer( many=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
  
 

    
    class Meta:
        model = Cart
        fields = ['id','user','items' ]
            
  
    
    
class  CarUpdatetSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    
    items = OrderSerializer(many=True)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
   
   
    
    class Meta:
        model = Cart
        fields = ['id','items','user' ]