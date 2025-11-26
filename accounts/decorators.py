from django.shortcuts import redirect
from functools import wraps

# Customer only
def customer_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is logged in AND is a customer
        if request.user.is_authenticated and getattr(request.user, 'user_type', None) == 'customer':
            return view_func(request, *args, **kwargs)
        # Redirect to login if not authorized
        return redirect('login')
    return wrapper

# Vendor only
def vendor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, 'user_type', None) == 'vendor':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
