from django.test import TestCase
from django.db import DataError, IntegrityError

from apps.products.models import CategoryModel, ProductModel

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = CategoryModel.objects.create(
            name = 'Produtos de Limpeza',
        )
    
    def test_create(self):
        self.assertEqual(self.category.name, 'Produtos de Limpeza')
        
    def test_name_max_length(self):
        self.category.name = 'a' * 33
         
        with self.assertRaises(DataError):
            self.category.save()
            
    def test_name_unique(self):
        with self.assertRaises(IntegrityError):
            CategoryModel.objects.create(
                name = 'Produtos de Limpeza',
            )
 
class ProductModelTest(TestCase):
    def setUp(self):
        self.category = CategoryModel.objects.create(
            name = 'Produtos de Limpeza',
        )
        
        self.product = ProductModel.objects.create(
            name = 'Esponja',
            category = self.category,
            barcode = '0123456789',
        )
        
    def test_create(self):
        self.assertEqual(self.product.name, 'Esponja')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.barcode, '0123456789')
        
    def test_name_max_length(self):
        self.product.name = 'a' * 33
        
        with self.assertRaises(DataError):
            self.product.save()

    def test_name_unique(self):
        with self.assertRaises(IntegrityError):
            ProductModel.objects.create(
                name = 'Esponja',
            )
            
    def test_category_on_delete(self):
        self.category.delete()
        self.product.refresh_from_db()
        
        self.assertEqual(self.product.category, None)
        
    def test_barcode_max_length(self):
        self.product.barcode = 'a' * 129
        
        with self.assertRaises(DataError):
            self.product.save()
            
    def test_barcode_unique(self):     
        with self.assertRaises(IntegrityError):
            ProductModel.objects.create(
                name = 'Detergente',
                barcode = '0123456789'
            )
            
    def test_barcode_null(self):   
        self.product.barcode = ''
        self.product.save()
        
        self.assertEqual(self.product.barcode, '')
        
    def test_barcode_blank(self): 
        self.product.barcode = None
        self.product.save()
        
        self.assertEqual(self.product.barcode, None)