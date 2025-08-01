from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_function(request):
    return render(request,'Application/Demo.html',{'nm':'Mohite'})
    # return HttpResponse("Hello World")
    
    