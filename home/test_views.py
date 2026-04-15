from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test accessibility on the home page view
    """
    def test_page_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
