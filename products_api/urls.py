from django.urls import path
from .views import ProductList,ProductDetail,ProductUpdate,CategoryList,ProductSortDevices,ProductSortAccessories,ProductSortGadgets

app_name='products_api'

urlpatterns = [
 
    #show all product
    path('all',ProductList.as_view(),name='listcreate_product'),
    #show individual product or delete it 
    path('<int:pk>/detail',ProductDetail.as_view(),name='detaildelete_product'),
    #update individual product 
    path('<int:pk>/update',ProductUpdate.as_view(),name='update_product'),
    path('category',CategoryList.as_view(),name='listcreate_category'),
    path('productsortby/devices',ProductSortDevices.as_view(),name='productsortby_devices'),
    path('productsortby/accessories',ProductSortAccessories.as_view(),name='productsortby_accessories'),
    path('productsortby/gadgets',ProductSortGadgets.as_view(),name='productsortby_gadgets'),
    
    
    
    
    
    ]
   