from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/clubs/', default='static/images/clubs/club-image.svg', verbose_name='Логотип')
    description = models.TextField(default="", verbose_name='Описание')
    vk = models.CharField(default="", blank=True, max_length=200, verbose_name='Ссылка на vk')
    telegram = models.CharField(default="", blank=True, max_length=200, verbose_name='Ссылка на telegram')
    ogs = models.CharField(default="", blank=True, max_length=200, verbose_name='Ссылка на ogs')
    contacts = models.TextField(default="", blank=True)
    is_visible = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клуб'
        verbose_name_plural = 'клубы'
