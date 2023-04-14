from django.urls import path
from .views import ProductList,ProductDetail,ProductUpdate

app_name='products_api'

urlpatterns = [
 
    #show all product
    path('',ProductList.as_view(),name='listcreate_product'),
    #show individual product or delete it 
    path('<int:pk>/detail',ProductDetail.as_view(),name='detaildelete_product'),
    #update individual product 
    path('<int:pk>/update',ProductUpdate.as_view(),name='update_product'),
    
    
    
    
    ]
   