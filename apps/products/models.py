from django.db import models

class CategoryModel(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
        db_table = 'category'    
    
    name = models.CharField(max_length = 32, unique = True)
    
    def __str__(self): return self.name
    
class ProductModel(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
        db_table = 'product'
    
    name = models.CharField(max_length = 32, unique = True)
    category = models.ForeignKey(CategoryModel, on_delete = models.SET_NULL, null = True, blank = True)
    barcode = models.CharField(max_length = 128, unique = True, null = True, blank = True)
    
    def __str__(self): return self.name