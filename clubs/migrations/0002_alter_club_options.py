# Generated by Django 4.2.17 on 2025-01-16 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name': 'клуб', 'verbose_name_plural': 'клубы'},
        ),
    ]