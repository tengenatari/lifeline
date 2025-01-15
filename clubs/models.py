from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'клуб'
        verbose_name_plural = 'клубы'
