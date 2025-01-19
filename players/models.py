from django.db import models
from django.utils import timezone


# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True, null=True)
    tournaments = models.CharField(max_length=100, blank=True, null=True)
    games = models.CharField(max_length=100, blank=True, null=True)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'
