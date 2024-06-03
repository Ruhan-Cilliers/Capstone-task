from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    """
    Render the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders home page called home.html.
    """
    return render(request, 'home.html')

def register(request):
    """
    This function handles user registration.

    If the request method is POST, the program attempts to process the registration form.
    If the form is valid, the program saves the user and redirects them to the login page.
    If the form is not valid, the program renders the registration form.
    If the request method is not POST, the program renders the registration form.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The registration page or the user is redirected to the login page.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)