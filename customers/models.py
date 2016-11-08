from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.username
