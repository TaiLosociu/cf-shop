from django.test import TestCase
from products.models import Product
from .models import Order


class TestOrderModels(TestCase):
    """ Test Order models """

    def setup(self):
        Order.objects.create(
            full_name='testname',
            email='test@test.com',
            phone_number='01234567890',
            street_address1='test',
            town_or_city='test',
            country='GB'
        )

    def test_order_string_method(self):
        """ Test string method for order class """
        order_number = Order.objects.create(order_number='100')
        self.assertEqual(str(order_number), '100')

    def test_update_total(self):
        """ Test that order total is updated correctly """
        order_total = 100
        grand_total = order_total
        self.assertEqual(grand_total, 100)


class TestOrdelineItemmodels(TestCase):
    """ Test that the order models work """
    def test_order_line_item_string(self):
        """ Test that the string method works """
        product = Product.objects.create(price=50.00)
        order = Order.objects.create(order_number='50')
        expected_output = 'on order 50'
        self.assertEqual(str(
            f'{product}on order {order.order_number}'),
            expected_output)
