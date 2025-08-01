from django.shortcuts import render
from datetime import datetime

# Create your views here.
def date_fun(request):
    current_datetime = datetime.now()
    return render(request,'app/datetask.html',{'current_datetime':current_datetime})
  