from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product, Category


# Create your views here.

def dummydata(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {}
    data['products'] = products
    data['categories'] = categories
    # return render(request, 'index.html', {'products': products}, {'categories': categories})
    return render(request, 'index.html', data)


1
