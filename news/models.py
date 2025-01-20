from django.db import models


# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
