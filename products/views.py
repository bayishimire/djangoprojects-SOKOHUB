from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from accounts.decorators import vendor_required
from django.contrib import messages

# Customer views
def product_list(request):
    products = Product.objects.filter(status='active')
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Vendor views
@vendor_required
def vendor_dashboard(request):
    products = Product.objects.filter(vendor=request.user).order_by('-created_at')
    total_products = products.count()
    active_products = products.filter(status='active').count()
    out_of_stock = products.filter(stock=0).count()

    context = {
        'products': products,
        'total_products': total_products,
        'active_products': active_products,
        'out_of_stock': out_of_stock,
    }
    return render(request, 'vendor_dashboard.html', context)

@vendor_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.status = 'active'
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect('vendor_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@vendor_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, vendor=request.user)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully!")
        return redirect('vendor_dashboard')

    return render(request, 'edit_product.html', {'form': form, 'product': product})

@vendor_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, vendor=request.user)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('vendor_dashboard')

    return render(request, 'confirm_delete.html', {'product': product})
