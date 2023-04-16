from rest_framework import serializers
from .models import Product,Category


class ProducttSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','title','description','published','price','sales','stock','image', 'category')
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')
        
        