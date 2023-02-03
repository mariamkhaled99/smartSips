from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='xwater'

# {% url 'app_name:urlname' %}

urlpatterns = [
    path('new',TemplateView.as_view(template_name="xwater/index.html")),
    path('', views.all_products, name='all_products'),
    path("product/<int:pk>", views.productinfo, name="productinfo"),
    
   
]