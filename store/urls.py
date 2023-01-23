from django.contrib import admin
from django.urls import path
from store.views import login, signup, home
from .views.home import Index
from .views.login import logout
from .views.cart import Cart

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', signup.SignUp.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart')
]


