from django.test import TestCase

from apps.products.models import CategoryModel, ProductModel
from apps.products.serializers import CategorySerializer, ProductSerializer

class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryModel.objects.create(
            name = 'Produtos de Limpeza',
        )
        
        self.serializer = CategorySerializer(instance = self.category)
        
    def test_create(self):
        self.assertEqual(self.serializer.data['id'], self.category.id)
        self.assertEqual(self.serializer.data['name'], self.category.name)

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryModel.objects.create(
            name = 'Produtos de Limpeza',
        )
        
        self.product = ProductModel.objects.create(
            name = 'Esponja',
            category = self.category,
            barcode = '0123456789',
        )
        
        self.serializer = ProductSerializer(instance = self.product)
        
    def test_create(self):
        self.assertEqual(self.serializer.data['id'], self.product.id)
        self.assertEqual(self.serializer.data['name'], self.product.name)
        self.assertEqual(self.serializer.data['category'], self.product.category.id)
        self.assertEqual(self.serializer.data['barcode'], self.product.barcode)