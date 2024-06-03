from django.urls import path
from . import views

app_name = 'band'
urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('songs/', views.song_list, name='song_list'),
    ]
"""
URL configuration for the band app.

Defines URL patterns for various pages of the band app, including the welcome page, about page, contact page, and song list page.

Attributes:
    app_name (str): The namespace for the band app URLs.

URL Patterns:
    - /welcome/: URL pattern for the welcome page.
    - /about/: URL pattern for the about page.
    - /contact/: URL pattern for the contact page.
    - /songs/: URL pattern for the song list page.

Each URL pattern is assigned to its corresponding view function.
"""