# Generated by Django 4.0.6 on 2022-08-08 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=45)),
                ('rendiment', models.IntegerField()),
                ('category', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=255)),
                ('ingredients', models.TextField(max_length=255)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
