from django.core.exceptions import ObjectDoesNotExist
from rest_framework.test import APITestCase
from ..models import Product
from rest_framework import status


class TestProduct(APITestCase):

    def setUp(self):
        Product.objects.create(name='test',
                               discount=50,
                               price_dc=100,
                               price_sale=50
        )

    def test_list(self):
        Product.objects.create(name='test2',
                               discount=50,
                               price_dc=200,
                               price_sale=100
        )
        responce = self.client.get('/products/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(len(responce.data), 2)

    def test_retrive(self):
        # /product/1
        ...

    def test_delete(self):
        responce = self.client.delete('/products/1/')
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)

        responce = self.client.delete('/products/1/')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)

        with self.assertRaises(ObjectDoesNotExist, msg='Объект не удалился из базы'):
            Product.objects.get(pk=1)


class TestCouponViewSet(APITestCase):

    def test_not_allowed_method(self):
        not_allowed_methods = {
            #'POST': self.client.post,
            'PUT': self.client.put,
            'PATCH': self.client.patch,
            'DELETE': self.client.delete,
            'GET': self.client.get
        }

        for method_name, method in not_allowed_methods.items():
            url = '/coupons/'
            responce = method(url)
            self.assertEqual(responce.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                             msg=f'Method {method_name} should be not allowed')

