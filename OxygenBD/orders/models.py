from django.db import models
from users.models import User
from catalog.models import ProductVariant

"""
Model architecture

Order
 ├── user (FK → User)
 ├── status (CharField)  # pending, paid, shipped, completed
 ├── total_price (DecimalField)
 ├── created_at (DateTimeField)

 OrderItem
 ├── order (FK → Order)
 ├── product_variant (FK → ProductVariant)
 ├── quantity (IntegerField)
 ├── price (DecimalField)  # фиксируем цену на момент покупки

"""

class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("completed", "Completed"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    total_price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0
)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Order Item"

    def __str__(self):
        return f"{self.product_variant} x{self.quantity}"