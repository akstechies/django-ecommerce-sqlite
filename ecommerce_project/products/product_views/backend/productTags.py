from django.shortcuts import render, redirect, get_object_or_404
from products.models import Tag
from products.forms import TagForm

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'backend/tag_list.html', {'tags': tags})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:tag_list')
    else:
        form = TagForm()
    return render(request, 'backend/tag_form.html', {'form': form, 'action': 'Create'})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('products:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'backend/tag_form.html', {'form': form, 'action': 'Update'})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('products:tag_list')
    return redirect('products:tag_list')
