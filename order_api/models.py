from django.db import models
from django.shortcuts import get_object_or_404
from user_api.models import CustomUser
from products_api.models import Product
from django.utils import timezone
from datetime import datetime ,timedelta


date_delivery=datetime.now()+timedelta(days=3) 
       

class Cart(models.Model):
    order_date=models.DateTimeField(default=timezone.now)
    delivery_date=models.DateTimeField(default=date_delivery,blank=True)
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
        
   
  

    

    
     
class LocationModel(models.Model):
    country = models.CharField(max_length=50, default="Egypt")

    def __str__(self):
        return self.country
    
class MonthModel(models.Model):
    month = models.CharField(max_length=50)

    def __str__(self):
        return self.month
    
class YearModel(models.Model):
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.year
    
class payment(models.Model):
    fullname=models.CharField(max_length=250,null=False)
    billingaddress=models.CharField(max_length=250,null=False)
    city=models.CharField(max_length=50,null=False)
    zipcode=models.CharField(max_length=6,null=False)
    country= models.ForeignKey(
        LocationModel,
        on_delete=models.CASCADE,
        null=False,
        related_name="country_name",
        default=1,
    )
    month= models.ForeignKey(
        MonthModel,
        on_delete=models.CASCADE,
        related_name="month_name",
        null=False,
        default=1
    )
    year= models.ForeignKey(
        YearModel,
        on_delete=models.CASCADE,
        related_name="year_name",
        null=False,
        default=1
    )
    
    cardholdername=models.CharField(max_length=250)
    
    cvv=models.CharField(max_length=3)
    cardnumber= models.CharField(
        null=False,
        max_length=16,
       )
    def __str__(self):
        return self.cardholdername
import uuid
class OrderInvoice(models.Model):
    cart=models.ForeignKey(Cart,blank=True,related_name='cart',on_delete=models.CASCADE)
    shipping=models.IntegerField(default=10)
    invoice_date=models.DateTimeField(default=timezone.now)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    @property
    def billto(self):
            billto=self.cart.user.username
            return billto
    @property
    def user_id(self):
            user_id=self.cart.user.id
            return user_id
        
        

    



    


    
        


