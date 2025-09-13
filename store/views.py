# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Product
from .cart import Cart

def product_list(request):
    products = Product.objects.all()
    cart = Cart(request)
    return render(request, 'product_list.html', {
        'products': products,
        'cart': cart,
        'cart_quantity': cart.get_total_quantity()
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart(request)
    return render(request, 'product_detail.html', {
        'product': product,
        'cart': cart,
        'cart_quantity': cart.get_total_quantity()
    })

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    update = request.POST.get('update', 'false') == 'true'
    cart.add(product, quantity=quantity, update_quantity=update)
    return redirect('store:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {
        'cart': cart,
        'cart_quantity': cart.get_total_quantity()
    })

@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('store:cart_detail')
