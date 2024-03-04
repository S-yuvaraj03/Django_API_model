# models.py
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_images/')
    location = models.CharField(max_length=200)

class Product(models.Model):
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

