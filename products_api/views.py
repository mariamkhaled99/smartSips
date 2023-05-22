
from rest_framework import generics
from .models import Product,Category,Wishlist
from .serializers import ProducttSerializer,CategorySerializer,WishlisttSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from user_api.models import CustomUser


# we can list and create items by this view 

class ProductCreate(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer
    # permission_classes = [IsAdminUser]
class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer
    permission_classes = [AllowAny]


# we can retrive and delete specific item by this view 
class ProductDetail(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    
    

#used to update some fields inside product table  
class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProducttSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "product updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
          
class ProductSortDevices(generics.ListAPIView):
    
    serializer_class=ProducttSerializer
    permission_classes = [AllowAny]
    
    
    def get_queryset(self):
        
        
        devices = Category.objects.get(name='Devices')

        # Here you can do the following thing:
        current_user = self.request.user

        # And use it as you wish in the filtering below:

        return Product.objects.filter(category=devices).order_by('title')
    
    
    
class ProductSortAccessories(generics.ListAPIView):
    
    serializer_class=ProducttSerializer
    permission_classes = [AllowAny]
    
    
    def get_queryset(self):
        
        
        Accessories = Category.objects.get(name='Accessories')

        # Here you can do the following thing:
        current_user = self.request.user

        # And use it as you wish in the filtering below:

        return Product.objects.filter(category=Accessories).order_by('title')


class ProductSortGadgets(generics.ListAPIView):
    
    serializer_class=ProducttSerializer
    permission_classes = [AllowAny]
    
    
    def get_queryset(self):
        
        
        Gadgets = Category.objects.get(name='Gadgets')

        # Here you can do the following thing:
        current_user = self.request.user

        # And use it as you wish in the filtering below:

        return Product.objects.filter(category=Gadgets).order_by('title')
        
        
# class ResearchSerializer(serializers.ModelSerializer):
#     templates = serializers.SerializerMethodField()

#     class Meta:
#         model = Research
#         fields = ('id', 'created', 'speaker', 'body', 'templates')

#     def get_templates(self, obj):
#         values = obj.get_values() # whatever your filter values are. obj is the Research instance
#         templates = ResearchTemplate.objects.filter(mergefields__contained_by=values) # Or whatever queryset filter
#         return ResearchTemplateSerializer(templates, many=True).data



class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes = [IsAdminUser]
    
    
    
class Add_wishlist(generics.CreateAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishlisttSerializer
    # permission_classes = [IsAuthenticated]
    
    
    # def validate(self, attrs):
    #     user_id = CustomUser.objects.get(id=id)
    #     product= get_object_or_404(Product,id=user_id)
    #     if product.user_wishlist.filter(id=user_id).exists():
    #         return Response("product already exist")
    #     else :
    #         id = attrs.get('id')
    #         title = attrs.get('title')
    #         price = attrs.get('price')
    #         stock= attrs.get('stock')
    #         image = attrs.get('image')
    #         category = attrs.get('category')
    #         user_wishlist = CustomUser.objects.get(id=id)
    #         user_wishlist.save()
    #         return user_wishlist
                
               
               
        
        
            
       
       
    

class Delete_wishlist(generics.DestroyAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishlisttSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class WishlistList(generics.ListAPIView):
    # queryset=Wishlist.objects.all()
    serializer_class=WishlisttSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'user_wishlist'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return Wishlist.objects.filter(user_wishlist=id)
    
    
    

from .serializers import ImageUploadSerializer

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return Category.objects.filter(id=id)