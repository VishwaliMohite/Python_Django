from django.shortcuts import render,redirect,get_object_or_404
from .models import Product

# Create your views here.
#Here we can able to see the list of products
def product_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list.html',{'products':products})

#Add a new productp
def add_product(request):
    if request.method =='POST':
        Product.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            description = request.POST['description'],
            stock = request.POST['stock'],
        )
        return redirect('product_list')
    return render(request,'products/add_product.html')  #it takes html file add_product.html from the prodects folder in templates and the send it to the browser

#Edit an existing product
def edit_product(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method =='POST':
        Product.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            description = request.POST['description'],
            stock = request.POST['stock'],
        )
        return redirect('product_list')
    return render(request,'products/edit_product.html',{'products':product})

# Delete a product
def delete_product(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method=='POST':
        product.delete()
        return redirect('product_list') 
    return render(request,'products/delete_product.html',{'products':product})