from django.contrib import admin
from django.urls import path
from store.views import dummydata

urlpatterns = [
    path('', dummydata)
]
