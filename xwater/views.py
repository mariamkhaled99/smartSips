from django.shortcuts import render
from .models import Category
from .models import Product


#-------------------crud by database----------------
# ----------get all object-------------------

# ----------get all Products-------------------
def all_products(request):
        products=Product.objects.all()
        context = {'allproducts': products}
        return render(request, 'xwater/main.html', context)
# ----------get all Categories-------------------
def all_categories(request):
        categories=Category.objects.all()
        context = {'allategories': categories}
        return render(request, 'xwater/main.html', context)
    
# ----------get a specific object-------------------
def productinfo(request,pk):
    product=Product.get_specific_object(pk)
#     product=Product.objects.get(pk=id)
    context = {"product": product}
   
    return render(request, "xwater/show.html", context)    

