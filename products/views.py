from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category


def all_products(request):
    """ Show all products, plus sorting and search quaries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(render(
                    request,
                    "You didn't enter any search criteria!"
                    ))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        context = {
            'products': products,
            'search_item': query,
            'currant_categories': categories,
            'current_sorting': f'{sort}_{direction}',
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View individual product detail """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product} )
