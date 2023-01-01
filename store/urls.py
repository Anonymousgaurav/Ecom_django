from django.contrib import admin
from django.urls import path
from store.views import homepage,signup

urlpatterns = [
    path('', homepage),
    path('signup', signup)
]
