from django.urls import path
from .views import OrderListSerializer,OrderDeleteSerializer,OrderDetailsListSerializer
app_name='order_api'

urlpatterns = [
 
    #show all product
    path('all',OrderListSerializer.as_view(),name='list_all_order'),
    #show individual product or delete it 
    path('<int:pk>/delete',OrderDeleteSerializer.as_view(),name='list_order'),
    #update individual product 
    path('<int:pk>/list',OrderDetailsListSerializer.as_view(),name='list_order'),
    
    
    
    
    ]
   