from django.shortcuts import render

# Create your views here.
# def itpreneur(request):
#     course_name = "Python Django"
#     course_duration = "6 monthes"
#     course_fee = "50,000"
#     course_description = "Learn Python, Django, HTML,CSS, JavaScript , and more"

#     course_details = {
#         "cname": course_name,
#         "cduration": course_duration,
#         "cfee": course_fee,
#         "cdescription": course_description,
#     }

#     return render(request, "core/itpreneur.html",course_details)

def filter_demo(request):
    context = {
        "name": "Vishwali",
        "students": ['Vishwali','jyoti','vaibhavi','lata'],
        "bio": '',
        # "today": date.today(),
        "description": "This is demo for filter in Django template",
        "colours":['red','green','blue','yellow'],
        "is_active": True,
        "Age": 22,
    }
    return render(request, "core/itpreneur.html",context)