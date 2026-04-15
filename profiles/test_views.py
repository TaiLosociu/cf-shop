from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from .models import UserProfile


class TestProfileView(TestCase):
    """ Test Cases """
    def setUp(self):
        """
        Set up info needed for testing
        """

        self.test_user = User.objects.create_user(
            username='testname',
            email='test@test.com',
            password='password',
        )

        self.test_user_profile = get_object_or_404(UserProfile,
                                                   user=self.test_user)

    def test_show_profile(self):
        """
        Test that user can access profile page when logged in
        """
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')
        self.client.logout()

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('accounts/login/')
