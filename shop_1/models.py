from django.db import models

# Create your models here.


class User(models.Model):
    pass


class Product(models.Model):
    TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables'),
    )

    image = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    discount = models.IntegerField()
    price_dc = models.FloatField()
    price_sale = models.FloatField()

    type = models.CharField(max_length=10, choices=TYPE)

    def __str__(self):
        return self.name
