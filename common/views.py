from django.shortcuts import render
from datetime import datetime
from random import randint
# Create your views here.

from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomView(View):
    def get(self, request):
        html = f'{randint(1, 100)}'
        return HttpResponse(html)


class HelloView(View):
    def get(self, request):
        html = f'<h1>Hello, World</h1>'
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')

