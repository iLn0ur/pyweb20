from django.urls import path
from .views import CurrentDateView, RandomView, HelloView, IndexView


urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('randint/', RandomView.as_view()),
    path('hello/', HelloView.as_view())
#    path('', IndexView.as_view())

]
