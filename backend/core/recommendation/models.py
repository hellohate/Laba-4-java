from django.db import models
from django.contrib.auth import get_user_model
class Genre(models.Model):
    name = models.CharField(max_length=150)

    objects = models.Manager()
class Movie(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    genres = models.ManyToManyField(
        'recommendation.Genre',
        related_name='movies',
    )

    objects = models.Manager()

class Watchlist(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='watchlists',
    )
    movie = models.ForeignKey(
        'recommendation.Movie',
        on_delete=models.CASCADE,
        related_name='watchlists',
    )

    date_added = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()