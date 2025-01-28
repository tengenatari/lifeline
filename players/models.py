from django.db import models
from django.utils import timezone


# Create your models here.


class Player(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город')
    rank = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ранг')
    rating = models.IntegerField(default=0, blank=True, verbose_name='Рейтинг')
    tournaments = models.IntegerField(default=0, blank=True, verbose_name='Турниры')
    games = models.IntegerField(default=0, blank=True, verbose_name='Игры')
    last_game_date = models.DateField(default='2000-01-01', blank=True, verbose_name='Дата последней игры')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка')
    is_visible = models.BooleanField(default=True, verbose_name='Отображать')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'
