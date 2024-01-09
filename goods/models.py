from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)