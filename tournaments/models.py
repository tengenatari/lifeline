from django.db import models


class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город')
    period = models.CharField(max_length=100, blank=True, null=True, verbose_name='Сроки проведения')
    date = models.DateField(default='2000-01-01', blank=True, verbose_name='Дата последней игры')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка')
    is_visible = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'турниры'
        verbose_name = 'турнир'
