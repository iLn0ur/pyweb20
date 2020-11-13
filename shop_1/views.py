from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Product
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin

from .settings.base import INFO

# Create your views here.


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        context = INFO
        return render(request, 'shop_1/index.html', context)


class ShopView(LoginRequiredMixin, View):
    def get(self, request, page=1):

        product_list = Product.objects.all()
        product_on_page = 2

        paginator = Paginator(product_list, product_on_page)

        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('shop'))

        context = {'page_obj': products_list}
        context.update(INFO)
        return render(request, 'shop_1/shop.html', context)


class AboutView(LoginRequiredMixin, View):

    def get(self, request):
        context = INFO
        return render(request, 'shop_1/about.html', context)


class ContactView(LoginRequiredMixin, View):

    def get(self, request):
        context = INFO
        return render(request, 'shop_1/contact.html', context)


class BlogView(LoginRequiredMixin, View):

    def get(self, request):
        context = INFO
        return render(request, 'shop_1/blog.html', context)


class WishlistView(LoginRequiredMixin, View):

    def get(self, request):
        context = INFO
        return render(request, 'shop_1/wishlist.html', context)