from django.contrib import admin
from django.urls import path
from store.views import homepage, signup, login

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup', signup),
    path('login', login)
]
