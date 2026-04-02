from django.db import models

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

# TODO complite user &  product_variant, when update user and catalog

class Order(models.Model):
    user = models.ForeignKey("app.Model", verbose_name="user", on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = "Order"

    def __str__(self):
        return f"{self.user} order: {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="Order", on_delete=models.CASCADE)
    product_variant = models.ForeignKey("", verbose_name="Product variant", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField( max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = "Order Item"

    def __str__(self):
        return self.order