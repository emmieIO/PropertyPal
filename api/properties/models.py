from django.db import models
from user.models import Landlord

# Create your models here.


class PropertyType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Property types"


class Property(models.Model):
    class Status(models.TextChoices):
        unavailable = "Unavailable", "Unavailable"
        available = "For Rent", "For rent"
        for_sale = "For Sale", "For Sale"

    property_name = models.CharField(max_length=50)
    address = models.CharField(
        max_length=150,
    )
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.ForeignKey(
        PropertyType, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(
        max_length=25, choices=Status.choices, default=Status.unavailable
    )
    payment_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"
