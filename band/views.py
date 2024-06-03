"""
This module contains view functions for rendering various pages of the website.

The views include:
- Welcome page
- About Us page
- Contact details page
- List of songs
"""

from django.shortcuts import render
from .models import Song

# Create your views here.

def welcome(request):
    """
    Render the welcome page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The welcome page.
    """
    return render(request, 'welcome.html')

def about(request):
    """
    Render the About Us page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The About Us page.
    """
    return render(request, 'About_us.html')

def contact(request):
    """
    Render the contact details page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The contact details page.
    """
    return render(request, 'contact_details.html')

def song_list(request):
    """
    Render a list of all songs.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The page with a list of songs.
    """
    songs = Song.objects.all()
    return render(request, 'About_us.html', {'songs': songs})
