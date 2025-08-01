from django.shortcuts import render
from .models import Student

def home(request):
    if Student.objects.count() == 0:  
        Student.objects.create(
            name="Vishwali",
            age=20,
            email="Vish@gmail.com"
        )
        Student.objects.create(
            name="Vishwa",
            age=21,
            email="Vish123@gmail.com"
        )

    students = Student.objects.all()
    return render(request, 'Myapp/home.html', {'students': students})
