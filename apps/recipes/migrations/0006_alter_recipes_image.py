# Generated by Django 4.1 on 2022-09-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%d/%m/%Y/'),
        ),
    ]