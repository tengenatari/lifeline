from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'города'
        verbose_name = 'город'


class Settings(models.Model):
    key = models.CharField(max_length=100, primary_key=True, verbose_name='Ключ')
    value = models.TextField(verbose_name='Значение')
    
    def __str__(self):
        return self.key

    def get_settings():
        settings_dict = dict()
        for setting in Settings.objects.values():
            settings_dict[setting["key"]] = setting["value"]
        return settings_dict
    
    class Meta:
        verbose_name_plural = 'настройки'
        verbose_name = 'настройка'