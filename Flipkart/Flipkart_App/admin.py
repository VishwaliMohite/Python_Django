from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','quantity')
    search_fields = ('name','description')
    list_filter = ('price',)