# Generated by Django 4.0.6 on 2022-08-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(upload_to='images/%d/%m/%Y/'),
        ),
    ]