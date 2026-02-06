from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    product_objects = Product.objects.all()
    
    # SEARCH FUNCTIONALITY
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(name__icontains=item_name)
        
    # PAGINATION
    paginator = Paginator(product_objects, 4)  # Show 8 products per page
    page = request.GET.get('page')
    
    # Get the products for the requested page
    try:
        product_objects = paginator.page(page)
    except PageNotAnInteger:
        product_objects = paginator.page(1)
    except EmptyPage:
        product_objects = paginator.page(paginator.num_pages)

    # RENDERING
    context = {
        'product_objects': product_objects
    }
    return render(request, 'shop/index.html', context)



def detail(request, pk):
    product_object = Product.objects.get(id=pk)
    
    context = {'product_object': product_object}
    
    return render(request, 'shop/detail.html', context)


def checkout(request):
    
    return render(request, 'shop/checkout.html')
