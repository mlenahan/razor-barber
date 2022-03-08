from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_service = models.BooleanField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    datetime = models.DateTimeField()
    barber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='barber_reservation_set')
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
