from django.contrib import admin
from .models import Order

# class OrderAdminSite(admin.ModelAdmin):
#     model=Order
#     fields=[ 'id','items','order_date']
#     list_display = ('id','order_date')
    
admin.site.register(Order)
