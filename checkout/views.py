from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product

# Create your views here.
def view_checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items():
                lineItem = OrderLineItem(order=order, quantity=quantity, product_id=product_id)
                lineItem.save()
                
            del request.session['cart']
            
        return redirect('home')
    
    else: 
        form = OrderForm()
        
    return render(request, 'checkout/checkout.html', {'form': form})