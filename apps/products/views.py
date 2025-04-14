from django.shortcuts import render, get_object_or_404
from apps.products.models import Product, Category, Images, Settings

def home(request):
    products = Product.objects.all()
    sliders = Product.objects.all()[:2]
    categories = Category.objects.all()[:6]
    settings = Settings.objects.latest('id')
    context = {
        'products':products,
        'sliders':sliders,
        'categories':categories,
        'settings': settings,
    }
    return render(request, 'index.html', context)

def content(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings,
    }
    return render(request, 'content.html', context)

def product_detail(request, slug):
    categories = Category.objects.all()[:6]
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product=product)
    context = {
        'categories':categories,
        'product':product,
        'images':images,
    }
    return render(request, 'pages/product-detail.html', context)


def category_detail(request, slug):
    categories = Category.objects.all()[:6]
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, status='True')
    context = {
        'categories':categories,
        'products':products,
        'category':category,
    }
    return render(request, 'pages/category-detail.html', context)


def contact(request):
    categories = Category.objects.all()[:6]
    return render(request, 'pages/contact.html', {'categories':categories})