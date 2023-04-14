
from rest_framework import generics
from .models import Product
from .serializers import ProducttSerializer
from rest_framework.response import Response


# we can list and create items by this view 
class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer


# we can retrive and delete specific item by this view 
class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProducttSerializer
    
#used to update some fields inside product table  
class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
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
        
        
# class ResearchSerializer(serializers.ModelSerializer):
#     templates = serializers.SerializerMethodField()

#     class Meta:
#         model = Research
#         fields = ('id', 'created', 'speaker', 'body', 'templates')

#     def get_templates(self, obj):
#         values = obj.get_values() # whatever your filter values are. obj is the Research instance
#         templates = ResearchTemplate.objects.filter(mergefields__contained_by=values) # Or whatever queryset filter
#         return ResearchTemplateSerializer(templates, many=True).data