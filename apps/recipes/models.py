from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Recipes(models.Model):
    person_name = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=45)
    duration = models.IntegerField()
    rendiment = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    description = models.TextField(max_length=528)
    ingredients = models.TextField(max_length=528)
    datetime = models.DateTimeField(default=datetime.now, blank=False)
    image = models.ImageField(upload_to='images/%d/%m/%Y/', blank=True)
    publicated = models.BooleanField(default=False)

    def __str__(self):
        return self.recipe_name
