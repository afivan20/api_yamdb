# Generated by Django 2.2.16 on 2021-11-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20211130_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]