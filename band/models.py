from django.db import models

# Create your models here.
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()  # Duration of the song in HH:MM:SS format
    release_date = models.DateField()

    def __str__(self):
        return self.title