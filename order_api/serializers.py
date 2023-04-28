from rest_framework import serializers
from .models import Order

                
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('id','total_items','total_price','stock','order_date', 'delivery_date','category')
        
        
       
    