from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name="status")
    image = models.CharField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Products for cats"


class Groups(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Groups"


class ProductsGroups(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Products groups"


class Prices(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Prices"
