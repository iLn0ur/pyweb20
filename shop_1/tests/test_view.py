from django.test import TestCase
from rest_framework import status
from django.test.utils import override_settings
from django.shortcuts import reverse


class TestShopView(TestCase):
    @override_settings(DEBUG=False)
    def test_get(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @override_settings(DEBUG=False)
    def test_get_reverse(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_used_templates(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'shop_1/shop.html')

    @override_settings(DEBUG=False)
    def test_get_reverse_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestIndexView(TestCase):
    @override_settings(DEBUG=False)
    def test_get_reverse_contact(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
