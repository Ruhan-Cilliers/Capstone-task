from django.urls import path
from . import views

app_name = 'band'
urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('songs/', views.song_list, name='song_list'),
    ]