from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product, Category
from store.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders' : orders})
