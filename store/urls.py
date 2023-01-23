from django.contrib import admin
from django.urls import path
from store.views import login, signup, home
from .views.home import Index

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', signup.SignUp.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login')
]
