from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
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
        login_input = request.POST.get('login_input')  # This will accept either email or username
        password = request.POST.get('password')

        # Check if the input is an email or username
        if '@' in login_input:
            # Input is an email
            try:
                user = User.objects.get(email=login_input)
                # Retrieve the username using the email
                username = user.username
            except User.DoesNotExist:
                username = None
        else:
            # Input is assumed to be a username
            username = login_input

        # Authenticate using the username (which could have been fetched by email or input directly)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Redirect to a home page or another page after successful login
            return redirect('index')
        else:
            # Handle the case where authentication fails
            error_message = "Invalid email/username or password"
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose another one.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return render(request, 'signup.html')
        
        # Create new user
        user = User.objects.create(
            username = username,
            email = email,
            password =  make_password(password),
            first_name = first_name,
            last_name = last_name
        )
        user.save()
        
        messages.success(request, 'Account created successfully! You can now log in.')
        # Redirect to the login page after successful signup
        return redirect('login')  
    # Show signup form
    return render(request, 'signup.html')  

@login_required
def logout(request):
    """Logs out the user and redirects to the home page."""
    auth_logout(request)
    # Redirect to a  'index' file 
    return redirect('index') 

def dashboard(request):
    pass

def profile(request):
    pass

def courses(request):
    pass
