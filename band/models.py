from django.db import models

# Create your models here.
    
class Song(models.Model):
    """
    A model representing a song object.

    Attributes:
        title (str): The name of the song.
        duration (timedelta): The duration of the song formated in HH:MM:SS.
        release_date (date): The release date of the song.

    Methods:
        __str__: Returns the title of the song as a string representation.
    """
    title = models.CharField(max_length=100)
    duration = models.DurationField()  # Duration of the song in HH:MM:SS format
    release_date = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the song.

        Returns:
            str: The title of the song.
        """
        return self.title