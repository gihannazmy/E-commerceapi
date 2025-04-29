from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.TextChoices):
    COMPUTERS = 'computers'
    FOOD = 'food'
    KIDS = 'kids'
    HOME = 'home'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000,blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    brand = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, choices=Category.choices)
    rating = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    comment = models.TextField(max_length=1000,blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment
