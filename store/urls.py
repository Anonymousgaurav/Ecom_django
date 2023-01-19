from django.contrib import admin
from django.urls import path
from store.views import homepage, SignUp, Login

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup', SignUp.as_view()),
    path('login', Login.as_view())
]
