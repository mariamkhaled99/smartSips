from rest_framework import serializers
from xwater.models import Product


class ProducttSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','title','description','published','price','status','image', 'category')
            