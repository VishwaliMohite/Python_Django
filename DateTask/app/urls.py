from django.contrib import admin
from django.urls import path
from .views import date_fun

urlpatterns = [
    path('admin/', admin.site.urls),
    path("date_fun/",date_fun,name="date_fun")
]
