# Generated by Django 4.2.17 on 2025-01-16 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('rank', models.CharField(blank=True, max_length=100, null=True)),
                ('tournaments', models.CharField(blank=True, max_length=100, null=True)),
                ('games', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'игрок',
                'verbose_name_plural': 'игроки',
            },
        ),
    ]