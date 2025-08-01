from django.contrib import admin
from django.urls import path
from .views import my_function

urlpatterns = [
    path('ys/',my_function),
]
