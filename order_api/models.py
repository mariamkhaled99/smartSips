from django.db import models
from django.shortcuts import get_object_or_404
from user_api.models import CustomUser
from products_api.models import Product
from django.utils import timezone
from datetime import datetime ,timedelta
# ,AdminProfile
# Create your models here.

date_delivery=datetime.now()+timedelta(days=3) 
class Order(models.Model):
    items=models.ManyToManyField(Product,blank=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
    
    def __str__(self):
        return self.user.username
      
    @property
    def amount(self):
        amount=self.items.count()
        return amount
    
    @property
    def total_price(self):
        total_price=0
        for item in self.items.all():
                
                total_price=item.price+total_price
        return total_price
    @property
    def address(self):
        address=self.user
        return address
    @property   
    def username(self):
        username=self.user.username
        return username
    
    @property
    def image(self):
        for item in self.items.all():
            image=item.image
            return image
    
    @property
    def category(self):
        for item in self.items.all():
            category=item.category.name
            return category
    
    @property
    def company(self):
        for item in self.items.all():
            
            company=item.admincompany
            return company
        
        
    
        
    
       
    #     return self.userAdminProfile.company
        
        
    # @property
    # def image(self):
        
    #     for item in self.items:
    #        image=item.image
       
    #     return image
       
    
   
        
    
# class OrderInvoice(models.Model):
#     order=models.ManyToManyField(Order,blank=True)
#     shipping=models.IntegerField(default=10)
    
   