from django.contrib import admin
from user_api.models import CustomUser,AdminProfile,Survey,UserProfile


# Register your models here.
# admin.site.register(admin)
admin.site.register(UserProfile)
admin.site.register(AdminProfile)
# admin.site.register(CustomUser)
admin.site.register(Survey)
class CustomUserAdminSite(admin.ModelAdmin):
    model=CustomUser
    fields=[ 'id','username','email','created_at']
    list_display = ('id','username','email','created_at')
    
admin.site.register(CustomUser,CustomUserAdminSite)
# ,'auth_source','auth_id','social_account',
# 'social_account',

