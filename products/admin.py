from django.contrib import admin
from .models import Product, Favorite

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price',)
    list_filter = ('category', 'price',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product')
