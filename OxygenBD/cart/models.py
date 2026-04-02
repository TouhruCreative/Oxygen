from django.db import models
from users.models import User
from catalog.models import ProductVariant
"""
Model architecture

Cart
 ├── user (OneToOne → User)
 ├── created_at (DateTimeField)

 CartItem
 ├── cart (FK → Cart)
 ├── product_variant (FK → ProductVariant)
 ├── quantity (IntegerField)

"""

class Cart(models.Model):
    user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_(""), on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, verbose_name=_(""), on_delete=models.CASCADE)
    quantity = models.IntegerField()