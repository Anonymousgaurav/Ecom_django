from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=500)

