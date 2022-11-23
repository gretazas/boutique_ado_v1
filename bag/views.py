from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product


def view_bag(request):
    ''' The view for the bag content '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' Add qnty to the product to shopping bag '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id]['items_id'] += quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

