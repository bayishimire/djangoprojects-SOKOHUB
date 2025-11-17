from django.urls import path
from .views import checkout, order_confirmation, order_history

urlpatterns = [
    path('checkout/<int:product_id>/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('my-orders/', order_history, name='order_history'),
]
