from django.urls import path,include
from .views import ImageUploadViewSet, ProductCreate,WishlistList,Delete_wishlist,Add_wishlist,ProductList,ProductDetail,ProductUpdate,CategoryList,ProductSortDevices,ProductSortAccessories,ProductSortGadgets
from rest_framework.routers import DefaultRouter
app_name='products_api'

router=DefaultRouter()
# router.register('user_register',UserViewSet,basename='user_register')
router.register(r'imageupload', ImageUploadViewSet)
urlpatterns = [
    path('', include(router.urls)),
 
    #show all product
    path('product/all',ProductList.as_view(),name='list_product'),
    path('product/add',ProductCreate.as_view(),name='product_add'),
    #show individual product or delete it 
    path('<int:pk>/detail',ProductDetail.as_view(),name='detaildelete_product'),
    #update individual product 
    path('<int:pk>/update',ProductUpdate.as_view(),name='update_product'),
    path('category',CategoryList.as_view(),name='listcreate_category'),
    path('productsortby/devices',ProductSortDevices.as_view(),name='productsortby_devices'),
    path('productsortby/accessories',ProductSortAccessories.as_view(),name='productsortby_accessories'),
    path('productsortby/gadgets',ProductSortGadgets.as_view(),name='productsortby_gadgets'),
    path('wishlist/add',Add_wishlist.as_view(),name='wishlist_add'),
    path('wishlist/delete/<int:pk>',Delete_wishlist.as_view(),name='wishlist_delete'),
    path('wishlist/list/<int:user_wishlist>',WishlistList.as_view(),name='wishlist_list'),
    
    
    
    
    
    ]
   