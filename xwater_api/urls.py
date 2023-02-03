from django.urls import path
from .views import ProductList,ProductDetail

app_name='xwater_api'

urlpatterns = [
 
    #show all product
   path('',ProductList.as_view(),name='listceate'),
    
    #show individual product
    path('<int:pk>/',ProductDetail.as_view(),name='detailcreate'),
   
]
