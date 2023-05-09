from django.contrib import admin
from user_api.models import CustomUser,Survey

# ,UserProfile,AdminProfile
# Register your models here.
# admin.site.register(admin)
# admin.site.register(UserProfile)
# admin.site.register(AdminProfile)
# admin.site.register(CustomUser)
admin.site.register(Survey)
class CustomUserAdminSite(admin.ModelAdmin):
    model=CustomUser
    fields=[ 'username','email','created_at']
    list_display = ('id','username','email','created_at')
    
admin.site.register(CustomUser,CustomUserAdminSite)


# class AdminProfileAdminSite(admin.ModelAdmin):
#     model=AdminProfile
#     fields=[ 'username','email','company']
#     list_display = ('id','username','email','company')
    
# admin.site.register(AdminProfile,AdminProfileAdminSite)
# ,'auth_source','auth_id','social_account',
# 'social_account',

