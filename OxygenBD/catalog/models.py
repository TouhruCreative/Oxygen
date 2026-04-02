from django.db import models
from shops.models import Shop
"""
Model architecture

Category
 ├── name (CharField)
 ├── parent (FK → Category, null=True)

Product
 ├── shop (FK → Shop)
 ├── category (FK → Category)
 ├── name (CharField)
 ├── description (TextField)
 ├── is_active (BooleanField)
 ├── created_at (DateTimeField)

ProductVariant  # SKU
 ├── product (FK → Product)
 ├── sku (CharField, unique)
 ├── price (DecimalField)
 ├── stock (IntegerField)
 ├── color (CharField)
 ├── size (CharField)

ProductImage
 ├── product (FK → Product)
 ├── image (ImageField)
 ├── is_main (BooleanField)
 
"""
# TODO complete parent
class Category(models.Model):

    name = models.CharField()
    parent = None
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("c")

    def str(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop, verbose_name=_(""), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_(""), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)
    sku = models.CharField(Product, max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    is_main = models.BooleanField()