from django.db import models
from .category import Category
  
  
class Product(models.Model):
    name = models.CharField(max_length=60)
    barcode = models.IntegerField(default=0)
    brand = models.CharField(max_length=60)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    price = models.IntegerField(default=0)
    available = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
   
  
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()
