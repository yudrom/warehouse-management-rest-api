# Generated by Django 5.1 on 2024-09-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='statuses',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='transactiontypes',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
