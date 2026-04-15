from django.test import TestCase
from products.models import Product, Category


class TestBagViews(TestCase):
    """ Test views in bag app """
    def setUp(self):
        self.category1 = Category.objects.create(
            name='testCategory', friendly_name='TestCategory')
        self.product1 = Product.objects.create(
            category=self.category1,
            name='testProduct',
            description='test',
            price='100',
            image='test',
        )

        self.quantity = 1

        self.cart_with_products = [{
            'product': str(self.product1.id),
            'quantity': int(self.quantity),
            'total': 123
        }]

    def test_view_cart_view(self):
        """ Test bag is visible """
        response = self.client.get('/bag/')
        self.assertTrue(response.status_code, 200)

    def test_add_to_cart_view(self):
        """ Test that item can be added to bag """
        cart_data = {
            'product': Product.objects.get(pk=self.product1.id),
            'quantity': int(self.quantity),
            'redirect_url': f'/products/{self.product1.id}/'
        }
        response = self.client.post(f'/bag/add/{self.product1.id}/',
                                    cart_data)
        self.assertEqual(response.status_code, 302)
