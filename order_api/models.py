from django.db import models
from django.shortcuts import get_object_or_404
from user_api.models import CustomUser
from products_api.models import Product
from django.utils import timezone
from datetime import datetime ,timedelta

# Create your models here.

date_delivery=datetime.now()+timedelta(days=3) 
class Order(models.Model):
    items=models.ManyToManyField(Product,blank=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
    
    def total_items(self):
        total_items=self.items.count()
        return total_items
    
    def total_price(self):
        for item in self.items:
            total_price=0
            total_price=item.price+total_price
        return total_price