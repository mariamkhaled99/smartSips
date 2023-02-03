from django.contrib import admin
from . import models


@admin.register(models.Product)
class Admin_xwater(admin.ModelAdmin):
    list_display=('id','title','description','published','price','status','image', 'category')
            
admin.site.register(models.Category)