from django.contrib import admin
from .models import Order,Cart,LocationModel,MonthModel,YearModel,payment,OrderInvoice
# ,payment
# 

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

class OrderInvoiceAdminSite(admin.ModelAdmin):
    model=OrderInvoice
    fields=[ 'invoice_date','shipping','cart']
    list_display = ('id','cart','billto','user_id','invoice_date','shipping')
    
admin.site.register(OrderInvoice,OrderInvoiceAdminSite)

admin.site.register(payment)
admin.site.register(LocationModel)
admin.site.register(MonthModel)
admin.site.register(YearModel)



