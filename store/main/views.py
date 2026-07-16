from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent=None)
    print("КАТЕГОРИИ:", categories)  # для проверки в терминале
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