from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'турниры'
        verbose_name = 'турнир'
