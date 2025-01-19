from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'города'
        verbose_name = 'город'
