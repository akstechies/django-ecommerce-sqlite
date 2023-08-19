from django.shortcuts import render

from .forms import ProductForm
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404

from .product_views.frontend.viewProducts import *
from .product_views.backend.productTags import *
from .product_views.backend.category import *

def product_list(request):
    products = Product.objects.all()
    return render(request, 'backend/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'backend/product_form.html', {'form': form, 'action': 'Create'})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':

        old_image_path = None
        if 'image' in request.FILES:
            old_image_path = product.image.path
        print(old_image_path)
            
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if old_image_path is not None:
                product.delete_old_image(old_image_path)
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'backend/product_form.html', {'form': form, 'action': 'Update'})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete_image()
        product.delete()
        return redirect('products:product_list')
    return redirect('products:product_list')
