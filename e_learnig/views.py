from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to a home page or another page after successful login
        else:
            # Handle the case where authentication fails
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

@login_required
def logout(request):
    """Logs out the user and redirects to the home page."""
    auth_logout(request)
    return redirect('index')  # Redirect to a view named 'index'
