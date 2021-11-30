# Generated by Django 2.2.16 on 2021-11-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20211130_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(verbose_name='Идентификатор жанра'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(verbose_name='Год произведения'),
        ),
    ]
