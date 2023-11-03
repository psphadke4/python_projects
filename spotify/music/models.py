from django.db import models

class Songs(models.Model):
    Genres=(
        ("ROCK","Rock"),
        ("POP","Pop"),
        ("INDIE", "Indie"),
        ("LOVE", "Love")
    )
    title=models.CharField(max_length=200)
    singer_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=140)
    song_file = models.FileField(upload_to='uploads')
    genre = models.CharField(max_length=30,choices=Genres)
    song_image = models.ImageField(default='default.jpg',upload_to='song_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'singer_name'], name='unique_migration_host_combination'
            )
        ]
        return f"{self.title}"






