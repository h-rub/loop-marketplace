from django.db import models
from django.conf import settings

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=50, null = False)

    def __str__(self):
        return self.status
    
class Currency(models.Model):
    singular_name = models.CharField(max_length=50, null = False)
    plural_name = models.CharField(max_length=50, null = False)
    symbol = models.CharField(max_length=10, null = False)
    std_int = models.CharField(max_length=10, null = False)

    def __str__(self):
        return f"{self.symbol} - {self.std_int}"

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete = models.PROTECT)
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"{self.title}"

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='product_photos')


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name