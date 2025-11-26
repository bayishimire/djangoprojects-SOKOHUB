from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomUserCreationForm
from accounts.decorators import vendor_required, customer_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['user_type']  
            user.save()
            login(request, user)

            if user.user_type == 'vendor':
                return redirect('vendor_dashboard')
            else:
                return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# Login view 
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')


@vendor_required
def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')

@customer_required
def product_list(request):
    return render(request, 'product_list.html')
