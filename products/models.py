from django.db import models
from django.contrib.auth.models import User
from datetime import time


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_service = models.BooleanField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_after_opening(start_datetime):
    # some condition
    # throw validation error
    pass

def validate_before_closing(end_datetime):
    # some condition
    # throw vcalidation error
    pass


HOUR_OF_DAY_24 = [(i, i) for i in range(1, 25)]


class Reservation(models.Model):
    opening_time = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
    closing_time = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
    barber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='barber_reservation_set')
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when a reservation is created, end datetime should be automatically infered
    # creating a reservation with a barber who already has a reservation during that timeframe should throw an exception
    # creating a reservation when user already has a reservation during that timeframe should throw an exception
    # creating a reservation that starts before operating hours should throw an exception
    # creating a reservation that ends after operating hours throws an exception
    def clean(self):
        # condition to check if barber has reservation during this timeframe
            # raise validation error
        # condition to check if user has reservation during this timeframe
            # raise validation error
        pass

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
