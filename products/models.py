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
        return f"id: {self.pk}, name: {self.name}"

    class Meta:
        verbose_name_plural="Products for cats"


class Groups(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    is_category = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Groups"

#FAKE MODEL
class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(Groups, on_delete=models.DO_NOTHING)
    is_category = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"
        db_table = "products_groups"
        managed = False


class ProductsGroups(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    group = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Products groups"


class Prices(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=21, decimal_places=2)
    sale_price = models.DecimalField(max_digits=21, decimal_places=2)
    margin = models.DecimalField(max_digits=21, decimal_places=2, default=20)
    curr = models.CharField(max_length=3, default='BYN')
    state = models.CharField(max_length=255, default='active')  #ACTIVE, DISABLE, DISCOUNT
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Prices"
