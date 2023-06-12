from django.urls import path
from .views import OrderListAllAPIView,OrderUpdateApiView,CartDeleteesApiView,CartListApiView,CartCreatesApiView,OrderListApiView,OrderDeleteApiView,OrderDetailsListApiView,OrderHistorysApiView,OrderCreatesApiView

app_name='order_api'

urlpatterns = [
 
    #show all product
    # path('first/add/cart',create_cart,name='create_cart_order'),
    path('<int:pk>/all',OrderListApiView.as_view(),name='list_all_order'),
    #show individual product or delete it 
    path('item/cart/delete/<int:pk>',OrderDeleteApiView.as_view(),name='delete-order'),
    path('item/cart/update/<int:pk>',OrderUpdateApiView.as_view(),name='update-order'),
    #update individual product 
    path('<int:pk>/list',OrderDetailsListApiView.as_view(),name='list_order'),
    path('order/history/<int:user>',OrderHistorysApiView.as_view(),name='history-all-order'),
    path('item/create',OrderCreatesApiView.as_view(),name='create-order'),
    path('cart/all/<int:user>',CartListApiView.as_view(),name='list-all-cart'),
    path('cart/create',CartCreatesApiView.as_view(),name='create-cart'),
    # path('cart/update/<int:pk>',CartUpdateApiView.as_view(),name='update-cart'),
    path('cart/delete/<int:pk>',CartDeleteesApiView.as_view(),name='delete-cart'),
    path('order/list/all',OrderListAllAPIView.as_view(),name='order-list'),
    
    
    
    
    
    
    ]
#    create_cart,,CartUpdateApiView

    