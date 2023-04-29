from django.urls import path
from .views import OrderListApiView,OrderDeleteApiView,OrderDetailsListApiView,OrderHistorysApiView
app_name='order_api'

urlpatterns = [
 
    #show all product
    path('all',OrderListApiView.as_view(),name='list_all_order'),
    #show individual product or delete it 
    path('<int:pk>/delete',OrderDeleteApiView.as_view(),name='list_order'),
    #update individual product 
    path('<int:pk>/list',OrderDetailsListApiView.as_view(),name='list_order'),
    path('order/history',OrderHistorysApiView.as_view(),name='history_all_order'),
    
    
    
    
    ]
   