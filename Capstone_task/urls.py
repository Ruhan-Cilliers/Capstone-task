"""
URL configuration for Capstone_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from band import views as band_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('band/', include('band.urls', namespace = 'band')),
    path('welcome/', band_views.welcome, name='welcome'),
    path('users/', include('users.urls', namespace = 'user')),
    path('register/', user_views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
"""
URL configuration for the Django project.

Defines URL patterns for all the functions and views created in this Django project.

URL Patterns:
    - /admin/: URL pattern for the Django admin.
    - /band/: URL pattern for URLs defined in the 'band' app.
    - /welcome/: URL pattern for the welcome page.
    - /users/: URL pattern for URLs created in the 'users' app.
    - /register/: URL pattern for the user registration page.
    - /: URL pattern for the login page and uses Django's built-in LoginView.
    - /logout/: URL pattern for the logout page and uses Django's built-in LogoutView.

Each URL pattern is assigned to the appropriate view.
"""