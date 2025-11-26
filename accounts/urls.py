from django.urls import path, include
from .views import register, CustomLoginView, logout_view

urlpatterns = [
 
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    
]
