from django.contrib import admin
from .models import Groups, ProductsGroups, Products, Prices

# Register your models here.

@admin.register(Groups)
class AdminGroups(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "id")


@admin.register(ProductsGroups)
class AdminProductsGroups(admin.ModelAdmin):
    list_display = ("product", "group")


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "image", "created_at", "updated_at", "id")


@admin.register(Prices)
class AdminPrices(admin.ModelAdmin):
    list_display = ("product", "price", "updated_at")