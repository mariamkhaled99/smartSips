
from django.db import models
# from django.contrib.auth.models import User # users associated with product
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from user_api.models import CustomUser
from django.utils.translation import gettext_lazy as _


def upload_to(instance,filename):
    return 'products/{filename}'.format(filename=filename)

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name

class Product(models.Model):
   
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description=models.TextField(null=True)
    published=models.DateTimeField(default=timezone.now)
    price=models.IntegerField()
    sales=models.IntegerField(default=0)
    stock=models.IntegerField(default=30)
    # need to fix image
    image=models.ImageField(upload_to='upload_to',default='products/default.jpg')

    
    class Meta:
        ordering=('-published',)
    def __str__(self) :
        return self.title
    
    def show_url(self):
        return reverse("productinfo",args=[self.id])
    
    def get_all_url(self):
        return reverse("productindex")
    
    
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
        
     
    @classmethod
    def get_specific_object(cls,id):
        return cls.objects.get(pk=id)
        # return get_object_or_404(cls,pk=id)
    
    def get_image_url(self):
        return f"/media/{self.image}"
             