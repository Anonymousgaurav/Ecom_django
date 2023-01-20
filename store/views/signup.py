from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product, Category
from store.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, phone, email, password)
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        isExists = customer.isExists()
        if isExists:
            error_message = "Email Address already Exists"
            return HttpResponse(error_message)
        else:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
