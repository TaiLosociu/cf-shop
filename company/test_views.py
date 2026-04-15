from django.test import TestCase
from .models import Contact, Newsletter


class TestContactViews(TestCase):
    """Tests views for the contact view """
    def test_contact_template(self):
        self.client.get('/''/')
        self.assertTemplateUsed('contact.html')


class TestAboutPage(TestCase):
    def test_about_template(self):
        """ Test about page is visible """
        self.client.get('/about/')
        self.assertTemplateUsed('about.html')
