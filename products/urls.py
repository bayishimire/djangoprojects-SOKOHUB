from django.urls import path
from .views import product_list, product_detail, vendor_dashboard, add_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('vendor/dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('vendor/add-product/', add_product, name='add_product'),
]
