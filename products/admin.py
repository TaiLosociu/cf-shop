from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'sku')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    search_fields = ('name',)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_by', 'stars', 'date_added')
    list_filter = ('stars', 'date_added')
    search_fields = ('product__name', 'created_by__username')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
