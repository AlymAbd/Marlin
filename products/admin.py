from django.contrib import admin
from .models import Groups, ProductsGroups, Products

# Register your models here.

@admin.register(Groups)
class AdminProductsGroups(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "id")

@admin.register(ProductsGroups)
class AdminProductsGroups(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "id")