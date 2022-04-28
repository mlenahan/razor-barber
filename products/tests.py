from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Reservation, Product


def setUp(self):
    barber = User.objects.create(username='j_gorman', password='password', first_name='Jonathan', last_name='Gorman')
    product = Product.objects.create(name='Fade', description='Fade haircut', price=25.00, is_service=True)
    user = User.objects.create(username='m_lenahan', password='password', first_name='Michael', last_name='Lenahan')
    Reservation.objects.create(opening_time=9, closing_time=17, barber=barber, product=product, user=user)


def test_create_reservation_instance(self):
    self.
    


# grab a test from blog for starting point
# when a reservation is created at 9.00am, the end datetime is set to 9.30am
# when a reservation with a barber who already has a 
    # reservation during that timeframe is created, a validation error is thrown

# when a reservation with a barber who does not have a 
    # reservation during that timeframe is created, a validation error is not thrown

# creating a reservation when user already has a reservation during that timeframe should throw an exception
    # test inverse
# creating a reservation that starts before operating hours should throw an exception
    # test inverse
# creating a reservation that ends after operating hours throws an exception
    # test inverse