from django.test import TestCase
from ..models import Product, User, Cart


class TestCart(TestCase):
    def test_str(self):
        user = User.objects.create()
        product = Product.objects.create()
        Cart.objects.create(user=user, product=product, count=1)
        cart = Cart.objects.get(pk=1)
        self.assertEqual(str(cart), '1 - User - Product')

    def test_unique_together(self):
        self.assertEqual(Cart.Meta.unique_together, (('user', 'product'),))
