from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)