from django.shortcuts import render
from .models import Song

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'About_us.html')

def contact(request):
    return render(request, 'contact_details.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'About_us.html', {'songs': songs})
