from django.db import models

# Create your models here.


class Tournament(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город')
    period = models.CharField(max_length=100, blank=True, null=True, verbose_name='Сроки проведения')
    date = models.DateField(default='2000-01-01', blank=True, verbose_name='Дата последней игры')
    is_visible = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'турниры'
        verbose_name = 'турнир'
