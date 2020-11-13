from django.db import models
from django.contrib.auth.models import User as UserAuth

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    auth_user = models.OneToOneField(UserAuth, null=True, on_delete=models.SET_NULL)

    age = models.IntegerField()


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


class Coupon(models.Model):
    name = models.CharField(max_length=25)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateField()
    finish_at = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:  # совместный первичный ключ
        unique_together = (('user', 'product'),)

    def __str__(self):
        return f'{self.id} - {self.user} - {self.product}'
