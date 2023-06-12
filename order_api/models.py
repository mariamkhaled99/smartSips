from django.db import models
from django.shortcuts import get_object_or_404
from user_api.models import CustomUser
from products_api.models import Product
from django.utils import timezone
from datetime import datetime ,timedelta
# ,AdminProfile
# Create your models here.

date_delivery=datetime.now()+timedelta(days=3) 
       

class Cart(models.Model):
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
    # order_item=models.ManyToManyField(Order,blank=True,related_name="items")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    shipping=models.IntegerField(default=10)
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
        
    # @property
    # def total_price(self):
    #     """for one item"""
    #     total_price=0
    #     for i in self.cart.items.all():
    #         total_price=(i.product.price*i.qnt)+total_price
    #     return total_price
        
  
   
    
    # def amount_of_products(self):
    #     """for all items"""
    #     amount=0
    #     for i in cartitems.items.all():
    #         amount=i.qnt+amount
    #     return amount
    # def total(self):
    #     """for one item"""
    #     total_price=0
    #     for i in cartitems.items.all():
    #         total_price=(i.product.price*i.qnt)+total_price
    #     return total_price

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='products')
    qnt=models.IntegerField(default=0)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='items')
    # class Meta:
    #     unique_together = ['cart','user']
    def __str__(self):
        return self.product.title
   
    
    
    @property
    def price(self):
        price=self.product.price
        return price
    
    @property
    def image(self):
    #     for item in self.items.all():
        image=self.product.image
        return image
    
    @property
    def category(self):
    #     for item in self.items.all():
        category=self.product.category.name
        return category
    
    @property
    def company(self):
        
    #     for item in self.items.all():   
        company=self.product.admincompany
        return company
    
    @property
    def Expected_date(self):
        
    #     for item in self.items.all():   
        Expected_date=self.cart.delivery_date
        return Expected_date
    
    @property
    def title(self):
        title=self.product.title
        return title
        
   
  

    

    
        
       
    
   
        
    
# class OrderInvoice(models.Model):
#     order=models.ManyToManyField(Order,blank=True)
#     shipping=models.IntegerField(default=10)
    


    
        


