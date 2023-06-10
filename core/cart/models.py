from django.db import models
from products.models import Product
from authentication.models import CustomUser
import datetime

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.pk}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.product}"
