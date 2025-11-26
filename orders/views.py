from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Order, OrderItem
from accounts.decorators import customer_required

@customer_required
def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        address = request.POST.get('delivery_address', '').strip()
        phone = request.POST.get('phone', '').strip()

        if not address or not phone:
            messages.error(request, "All fields are required")
            return redirect('checkout', product_id=product.id)

        if quantity > product.stock:
            messages.error(request, "Not enough stock available")
            return redirect('checkout', product_id=product.id)

        total = quantity * product.price

        order = Order.objects.create(
            customer=request.user,
            total=total,
            delivery_address=address,
            phone=phone
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

        product.stock -= quantity
        product.save()

        messages.success(request, "Order placed successfully!")
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'checkout.html', {'product': product})


@customer_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})



@customer_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    
    # Pre calculate counts
    total_orders = orders.count()
    pending_orders = orders.filter(status='pending').count()
    completed_orders = orders.filter(status='completed').count()

    context = {
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'order_history.html', context)
