from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product, Category
from store.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models.product import Product


class Cart(View):
    # overiding get method in class based view
    # code to handle get responses
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
