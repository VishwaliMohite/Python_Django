from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Django!")

def my_func(request):
    return HttpResponse("Hii from Django")