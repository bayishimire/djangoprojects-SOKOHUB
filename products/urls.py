from django.urls import path
from .views import (
    product_list,
    product_detail,
    vendor_dashboard,
    add_product,
    edit_product,
    delete_product
)

urlpatterns = [
    # Customer routes
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),

    # Vendor routes
    path('vendor/dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('vendor/add-product/', add_product, name='add_product'),
    path('vendor/edit/<int:pk>/', edit_product, name='edit_product'),
    path('vendor/delete/<int:pk>/', delete_product, name='delete_product'),
]
