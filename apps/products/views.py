from rest_framework import viewsets

from apps.products.models import CategoryModel, ProductModel
from apps.products.serializers import CategorySerializer, ProductSerializer
from apps.products.filters import CategoryFilter, ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    
    search_fields = ['name']
    ordering_fields = '__all__'
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    search_fields = ['name', 'gtin']
    ordering_fields = '__all__'