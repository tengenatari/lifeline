from django.db import models


# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
