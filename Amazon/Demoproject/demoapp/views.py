from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Application/home.html')

def contact(request):
    return render(request,'Application/contact.html')

def product(request):
    return render(request,'Application/product.html')