from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ Model for contact form """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Contact Form'
        ordering = ['-created_on']


class Newsletter(models.Model):
    """ Model for newletter """
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.email)
