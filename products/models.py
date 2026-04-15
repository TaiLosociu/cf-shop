from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Category model """
    class Meta:
        """ use a verbose name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(
        max_length=254, null=True, blank=False, unique=True
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
        )

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """ Model for reviews """
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField(default=3)
    date_added = models.DateTimeField(auto_now_add=True)


