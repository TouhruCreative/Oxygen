from django.db import models
from users.models import User
"""
Model architecture

Shop
 ├── owner (OneToOne → User)
 ├── name (CharField)
 ├── description (TextField)
 ├── rating (FloatField)
 ├── created_at (DateTimeField)
"""

class Shop(models.Model):

    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name="Shop name")
    description = models.TextField()
    rating = models.FloatField()
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = "Shop"

    def __str__(self):
        return self.name