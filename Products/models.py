# from django.db import models
# from django.conf import settings


# class Product(models.Model):
#     STATUS_CHOICES = (
#         ("active", "Active"),
#         ("inactive", "Inactive"),
#     )

#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="products"
#     )

#     product_name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     category = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100, blank=True)

#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     stock = models.PositiveIntegerField(default=0)

#     image = models.ImageField(upload_to="products/")

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default="active"
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-created_at"]

#     def __str__(self):
#         return f"{self.product_name} - {self.owner.unique_id}"

from django.conf import settings
from django.db import models

class Product(models.Model):
    assigned_user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="assigned_products",
    null=True,
    blank=True,
      )

    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()

    image = models.ImageField(upload_to="products/")

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("packaging", "Packaging"),
        ("shipped", "Shipped"),
        ("delivery", "Delivery"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )