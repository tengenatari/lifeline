from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    count_of_tournaments = models.CharField(max_length=100)
    count_of_matches = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'
