from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages
from profiles.models import User
from .models import Product, Category
from .forms import ProductForm


class Test_ProductViews(TestCase):
    """ Test the views in the products app """

    def setUp(self):
        """ Set up info neede for testing """
        self.category1 = Category.objects.create(
            name='testcategory', friendly_name='Testcategory')
        self.product1 = Product.objects.create(
            category=self.category1,
            name='testProduct',
            description='test',
            price='100',
            rating='5.00',
            image='test')
        self.admin_user = User.objects.create_superuser(
            username='admin', password='adminpassword',
            email='admin@admin.com')
        self.user = User.objects.create_user(
            username='user', password='password', email='test@test.com')

    def test_all_products_view(self):
        """ Test that users can view products page """
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """ Test that users can view products detail page """
        response = self.client.get(f'/products/{self.product1.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_product_view(self):
        """ Test that only admin can access add product page """
        self.client.force_login(self.admin_user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        self.client.force_login(self.user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product_view(self):
        """ Test that only admin can access edit product page """
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        self.client.force_login(self.user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_product_works_for_admin(self):
        """ Test that admin can delete products """
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/delete/{self.product1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Product deleted!')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_delete_product_dosent_work_for_non_admin(self):
        """ Test that non admin cannot delete products """
        self.client.force_login(self.user)
        response = self.client.get(f'/products/delete/{self.product1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only store owners can do that.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()
