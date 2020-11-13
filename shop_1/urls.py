from django.urls import path
from .views import IndexView, ShopView, WishlistView, ContactView, AboutView, BlogView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page>', ShopView.as_view(), name='shop'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
]