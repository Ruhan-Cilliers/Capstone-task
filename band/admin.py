from django.contrib import admin
from .models import Song

# Register your models here.

"""
Admin registration for the Song model.

This registers the Song model with the Django admin interface, allowing it to be managed through the admin site.
"""
admin.site.register(Song)