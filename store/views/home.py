from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product, Category
from store.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from django.views import View


# Create your views here


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
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
        print('You are :', request.session.get('customer_email'))
        return render(request, 'index.html', data)
