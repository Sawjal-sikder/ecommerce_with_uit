from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'product_details.html', context)