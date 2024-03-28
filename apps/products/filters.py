from django_filters import rest_framework as filters

from apps.products.models import CategoryModel, ProductModel

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = CategoryModel
        
        fields = {
            'id': ['exact'],
        }
        
class ProductFilter(filters.FilterSet):
    class Meta:
        model = ProductModel
        
        fields = {
            'id': ['exact'],
            'category': ['exact'],
        }