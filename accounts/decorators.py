from django.shortcuts import redirect
from functools import wraps

def vendor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'vendor':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def customer_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'customer':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
