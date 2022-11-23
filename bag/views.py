from django.shortcuts import render

def view_bag(request):
    ''' The view for the bag content '''
    return render(request, 'bag/bag.html')
