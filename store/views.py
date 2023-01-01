from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product, Category


# Create your views here.

def homepage(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    # return render(request, 'index.html', {'products': products}, {'categories': categories})
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return HttpResponse(request.POST)
