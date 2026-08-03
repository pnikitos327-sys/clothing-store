from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart, product=product, quantity=1)
    return redirect('cart')

def home(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent=None)
    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    subcategories = Category.objects.filter(parent=category)
    categories = Category.objects.filter(parent=None)
    return render(request, 'category.html', {
        'category': category,
        'products': products,
        'subcategories': subcategories,
        'categories': categories,
    })

def cart_view(request):
    return render(request, 'cart.html')