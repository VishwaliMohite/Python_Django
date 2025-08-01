from django.urls import path
from . import views

urlPatterns = [
    path('',views.product_list, name='product_list'),     #List all product
    path('add/',views.add_product,name='add_product'),    # add new product
    path('edit/<int:id>',views.edit_product,name='edit_product'),   #Edit an existing product
    path('delete/<int:id>',views.delete_product,name='delete_product'),  # Delete a product
]