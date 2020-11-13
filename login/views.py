from django.shortcuts import render
from datetime import datetime
from random import randint

from django.http import JsonResponse
# Create your views here.

from django.views import View
from django.http import HttpResponse


class LoginView(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        return JsonResponse(request.POST)

