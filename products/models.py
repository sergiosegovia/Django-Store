from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from customers.models import Customer

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products', blank=True)
    slug = AutoSlugField(populate_from='name')
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'favorites'

    def __str__(self):
        return '%s' % (self.product.name)
