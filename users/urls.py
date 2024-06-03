from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]
"""
URL configuration for the login app.

Defines URL patterns for the login app, including the home page and registration page.

Attributes:
    app_name (str): The namespace for the login app URLs.

URL Patterns:
    - /home/: URL pattern for the home page.
    - /register/: URL pattern for the registration page.

Each URL pattern is has been assigned to its corresponding view function.
"""