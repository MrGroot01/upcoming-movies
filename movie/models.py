from django.db import models
from datetime import date

class Movie(models.Model):

    # ✅ Manual ID
    id = models.AutoField(primary_key=True)

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Sci-Fi', 'Sci-Fi'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Telugu', 'Telugu'),
        ('Kannada','Kannada')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    poster = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    duration = models.IntegerField(help_text="Duration in minutes")

    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
        default='English'
    )

    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default='Action'
    )

    is_upcoming = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.is_upcoming = self.release_date >= date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title