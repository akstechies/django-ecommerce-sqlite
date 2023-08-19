from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart:cart_view')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
            form_errors = form.errors
    else:
        form = UserCreationForm()
        form_errors = None
    return render(request, 'register.html', {'form': form, 'form_errors': form_errors})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cart:cart_view')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/auth/login/')
def logout_view(request):
    logout(request)
    return redirect('login')
