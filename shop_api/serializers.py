from rest_framework import serializers
from .models import User, Product, Coupon, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # сериализатор должен работать с моделью User из models.py
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # сериализатор должен работать с моделью Product из models.py
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon  # сериализатор должен работать с моделью Coupon из models.py
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart  # сериализатор должен работать с моделью Cart из models.py
        fields = '__all__'
