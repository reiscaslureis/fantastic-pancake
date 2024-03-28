from rest_framework import serializers

from apps.products.models import CategoryModel, ProductModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CategoryModel
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductModel