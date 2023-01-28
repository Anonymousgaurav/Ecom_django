from django.contrib import admin
from .models import Product, Category
from .models.customer import Customer
from .models.orders import Order


# Register your models here.
# Encapsulate all admin options and functionality for a given model.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
