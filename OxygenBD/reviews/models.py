from django.db import models
from users.models import User
from catalog.models import Product

"""
Model architecture


Review
 ├── user (FK → User)
 ├── product (FK → Product)
 ├── rating (IntegerField)
 ├── text (TextField)
 ├── created_at (DateTimeField)
 
 """

class Review(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField() 
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
    
    def __str__():
        return f"{self.user} rated {self.product}: {self.rating}"