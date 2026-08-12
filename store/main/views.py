from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Product, Category, Cart, CartItem, ProductImage
from .forms import RegistrationForm

def registersion_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

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
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        items = CartItem.objects.filter(cart=cart)
        total = sum(item.product.price * item.quantity for item in items)
    else:
        items = []
        total = 0
    return render(request, 'cart.html', {'items': items, 'total': total})

def product_delait(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = ProductImage.objects.filter(product=product)  
    return render(request, 'product.html', {
        'product': product,
        'images': images,
    })