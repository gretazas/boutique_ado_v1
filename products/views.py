from django.shortcuts import render
from .models import Product


def all_products(request):
    """ Show all products, plus sorting and search quaries """
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

