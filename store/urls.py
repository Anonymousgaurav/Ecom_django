from django.contrib import admin
from django.urls import path
from store.views import login, signup, home

urlpatterns = [
    path('', home.homepage, name='homepage'),
    path('signup', signup.SignUp.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login')
]
