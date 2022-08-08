from django.db import models
from datetime import datetime


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=45)
    rendiment = models.IntegerField()
    category = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    ingredients = models.TextField(max_length=255)
    datetime = models.DateTimeField(default=datetime.now, blank=False)
