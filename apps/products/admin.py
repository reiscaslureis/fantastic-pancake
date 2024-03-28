from django.contrib import admin

from apps.products.models import CategoryModel, ProductModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'barcode']