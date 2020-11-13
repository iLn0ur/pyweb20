from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet  # вариант импорта
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework import status
from shop_1.views import ShopView


from .models import User, Product, Coupon, Cart
from .serializers import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
                # queryset - это набор из базы данных которые будут сериаиловаться -
                # т.е выбраны из базы данных и будут переданы в json
    """
    queryset = User.objects.all()  #queryset - это набор из базы данных которые будут сериаиловаться -
                                    # т.е выбраны из базы данных и будут переданы в json
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  #queryset - это набор из базы данных которые будут сериаиловаться -
                                    # т.е выбраны из базы данных и будут переданы в json
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        filter_params = {param: request.GET[param] for param in request.GET}
        '''param - название поле словаря и из requst получаем его значение,
            таким образом получаем словарь и сопоставляем его со значениями из БД'''
        queryset = self.get_queryset()  # питоновский объект, который мы далее сериализуем
        filter_queryset = queryset.filter(**filter_params)
        serializer = self.get_serializer(filter_queryset, many=True)
        return Response(serializer.data)


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CartViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,  # показать одну корзину
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    """
    API for carbage

    list: и для получения списка корзины
    add: добавление в корзинку вкусняшек конкретному пользователю
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # получить данные из браузера
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def add(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.GET['user'])
        count = request.GET['count']

        queryset = self.get_queryset()
        serializer = self.get_serializer(data=dict(user=user.pk, product=product.pk, count=count))
        serializer.is_valid(raise_exception=True)

        queryset.create(user=user, product=product, count=count)

        # return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return ShopView().get(page=1)
