from django.contrib import admin
from .models import Order,Cart
# 

# class OrderAdminSite(admin.ModelAdmin):
#     model=Order
#     fields=[ 'id','items','order_date']
#     list_display = ('id','order_date')
class CartAdminSite(admin.ModelAdmin):
    model=Cart
    fields=[ 'delivery_date','user' ,'order_date']
    list_display = ('id', 'delivery_date','user','order_date','address','username')
    
admin.site.register(Cart,CartAdminSite)

class OrderAdminSite(admin.ModelAdmin):
    model=Order
    fields=[ 'product','qnt','cart']
    list_display = ('id','product','qnt','cart','price','image','category','company')
    
admin.site.register(Order,OrderAdminSite)


