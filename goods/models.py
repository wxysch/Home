from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

class Products(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='goods_images',blank=True,null=True)
    price = models.DecimalField(default=0.00, max_digits = 7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits = 7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories,on_delete = models.CASCADE)