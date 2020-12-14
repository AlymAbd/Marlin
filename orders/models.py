from django.db import models
from django.contrib.auth.models import User
from products.models import Products, Prices

# Create your models here.

class Order(models.Model):
    amount = models.DecimalField(max_digits=17, decimal_places=2)
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    contacts = models.ForeignKey('Contacts', on_delete=models.DO_NOTHING)


class ProductOrders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    price = models.ForeignKey(Prices, on_delete=models.DO_NOTHING)


class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Contacts(models.Model):
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=25)
    home_number = models.CharField(max_length=8)
    flat = models.CharField(max_length=4, blank=True, null=True)
    comments = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
