from rest_framework import serializers
from .models import Product,Category,Wishlist
from user_api.models import CustomUser


class ProducttSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','title','description','published','price','sales','stock','image', 'category','admincompany')
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')
        
        
class WishlisttSerializer(serializers.ModelSerializer):
    # id=
    # title
    # price
    # stock
    # image
    # category
    class Meta:
        model=Wishlist
        fields=('id','product','user_wishlist')
        