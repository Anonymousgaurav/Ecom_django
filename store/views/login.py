from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product, Category
from store.models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Login(View):
    # overiding get method in class based view
    # code to handle get responses
    def get(self, request):
        return render(request, 'login.html')

    # overiding post method in class based view
    # code to handle post responses
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_details(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('homepage')
            else:
                return HttpResponse("Your Password is wrong")

        else:
            return HttpResponse("Check your login details")


def logout(request):
    request.session.clear()
    return redirect('login')
