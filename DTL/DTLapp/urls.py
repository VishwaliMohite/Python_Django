from django.contrib import admin
from django.urls import path
from .views import filter_demo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('itpreneur/',itpreneur, name='itpreneur'),
    path('filter_demo/',filter_demo, name='filter_demo'),
]
