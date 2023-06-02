from django.contrib import admin
from user_api.models import CustomUser,Survey

# Register your models here.

# admin.site.register(CustomUser)
admin.site.register(Survey)
class CustomUserAdminSite(admin.ModelAdmin):
    model=CustomUser
    fields=[ 'username','email','created_at','profile_photo','phone_number','city','company','address','password','is_normal','is_superuser']
    list_display = ('id','username','email','created_at','profile_photo','phone_number','city','company','address','password','is_normal','is_superuser')
    
admin.site.register(CustomUser,CustomUserAdminSite)


#

