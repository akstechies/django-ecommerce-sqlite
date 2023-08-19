from django.shortcuts import get_object_or_404, render
from products.models import Product

def view_product_list(request):
    products = Product.objects.all()
    return render(request, 'frontend/product_list.html', {'products': products})

def view_product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'frontend/product_detail.html', {'product': product})