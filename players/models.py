from django.db import models
from django.utils import timezone


# Create your models here.


class Player(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='')
    rank = models.CharField(max_length=100, blank=True, null=True, verbose_name='')
    raiting = models.CharField(max_length=100, blank=True, null=True)
    tournaments = models.CharField(max_length=100, blank=True, null=True)
    games = models.CharField(max_length=100, blank=True, null=True)

    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'
