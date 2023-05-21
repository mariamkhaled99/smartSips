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
    item=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='items')
    qnt=models.IntegerField(default=1)
    
    # cart=models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='carts')
    # class Meta:
        # unique_together = ['cart','user']
    def __str__(self):
        return self.item.title
   
    
    
    @property
    def price(self):
        price=self.item.price
        return price
    
    @property
    def image(self):
    #     for item in self.items.all():
        image=self.item.image
        return image
    
    @property
    def category(self):
    #     for item in self.items.all():
        category=self.item.category.name
        return category
    
    @property
    def company(self):
        
    #     for item in self.items.all():   
        company=self.item.admincompany
        return company
  
    
    # @property
    # def image(self):
    #     for item in self.items.all():
    #         image=item.image
    #         return image
    
    # @property
    # def category(self):
    #     for item in self.items.all():
    #         category=item.category.name
    #         return category
    
    # @property
    # def company(self):
    #     for item in self.items.all():
            
    #         company=item.admincompany
    #         return company
        

    
class Cart(models.Model):
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
    order_item=models.ManyToManyField(Order,blank=True,related_name="items")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
   

    @property
    def address(self):

            address=self.user.address
            return address
    @address.setter
    def address(self, new_address):
        self._address = new_address
       
        
    @property
    def username(self):
            username=self.user.username
            return username
 
    @username.setter
    def username(self, new_username):
        self._username = new_username
        
    @property
    def total_price(self):
        total_price=0
        for i in self.order_item.all():        
            total_price=(i.item.price*i.qnt)+total_price
        return total_price
    
    # @property
    # def amount(self):
    #     if self.order_item==None:
    #         return 0
    #     amount=0
    #     for i in self.order_item.all():        
    #         amount=i.qnt+amount
    #     return amount
    
    
        
       
    
   
        
    
# class OrderInvoice(models.Model):
#     order=models.ManyToManyField(Order,blank=True)
#     shipping=models.IntegerField(default=10)
    


    
        


