from django.contrib import admin
from .models import Groups, ProductsGroups, Products, Prices, Categories

# Register your models here.

@admin.register(Groups)
class AdminGroups(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_active", "id", "is_category", "parent_id")

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_active", "id", "is_category", "parent_id")

@admin.register(ProductsGroups)
class AdminProductsGroups(admin.ModelAdmin):
    list_display = ("id", "product", "group")


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_active", "image", "created_at", "updated_at")


@admin.register(Prices)
class AdminPrices(admin.ModelAdmin):
    list_display = ("id", "product", "purchase_price", "sale_price", "margin", "curr", "state", "created_at", "updated_at")