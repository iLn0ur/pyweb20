from django.test import TestCase
from rest_framework import status


class TestApi(TestCase):
    def test_api_URL(self):
        responce = self.client.get('/api/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
