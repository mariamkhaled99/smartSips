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
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
# class OrderInvoice(models.Model):
#     order=models.ManyToManyField(Order,blank=True)
#     shipping=models.IntegerField(default=10)
    
   