from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]