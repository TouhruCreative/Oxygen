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
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Cart"
    
    def str():
        return f"{self.user} cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Cart", on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, verbose_name="Product Variant", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Cart"
    
    def __str__(self):
        return f"{self.cart}"