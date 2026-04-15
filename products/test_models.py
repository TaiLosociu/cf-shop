from django.test import TestCase
from .models import Category, Product


class TestProductModels(TestCase):
    """ That prodcuts work """
    fixtures = ['categories.json', 'products.json']

    def test_product_name(self):
        """ Test product name  """
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, 'Lavazza Oro')
        self.assertNotEqual(product.name, 'Test name')
        self.assertEqual(str(product), product.name)

    def test_product_description(self):
        """ Test product description """
        product = Product.objects.get(pk=1)
        self.assertEqual(
            product.description, (
                 "The Lavazza coffee beans are a blend of Arabica from Brazil,\
                RainForest certified. Enjoy a strong coffee with gourmet\
                notes of cereals and dried fruit. 1kg."))
        self.assertNotEqual(product.description, 'test description')


class TestCategoryModels(TestCase):
    """ Test that categories works """
    fixtures = ['categories.json']

    def test_category_name(self):
        """ Test category name """
        category = Category.objects.get(pk=1)
        self.assertEqual(category.name, 'Beans')
        self.assertNotEqual(category.name, 'test')
        self.assertEqual(str(category), category.name)

    def test_category_friendly_name(self):
        """ Test category friendly name """
        category = Category.objects.get(pk=5)
        self.assertEqual(category.friendly_name, 'Beans')
        self.assertNotEqual(category.friendly_name, 'Test Category')
        self.assertEqual(
            Category.get_friendly_name(category), category.friendly_name)
