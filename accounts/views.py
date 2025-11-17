# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm

#== Register view==
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'vendor':
                return redirect('vendor_dashboard')
            else:
                return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# ==Login view==
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout view (GET logout)
def logout_view(request):
    logout(request)
    return redirect('home') 
