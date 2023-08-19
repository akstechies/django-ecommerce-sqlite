from django.shortcuts import render, redirect, get_object_or_404
from products.models import Category
from products.forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'backend/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    return render(request, 'backend/category_form.html', {'form': form, 'action': 'Create'})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'backend/category_form.html', {'form': form, 'action': 'Update'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('products:category_list')
    return redirect('products:category_list')