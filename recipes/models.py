from django.db import models
from datetime import datetime
from persons.models import Person


class Recipes(models.Model):
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=45)
    duration = models.IntegerField()
    rendiment = models.IntegerField()
    category = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    ingredients = models.TextField(max_length=255)
    datetime = models.DateTimeField(default=datetime.now, blank=False)
    image = models.ImageField(upload_to='images/%d/%m/%Y/', blank=False)
    publicated = models.BooleanField(default=False)

    def __str__(self):
        return self.recipe_name
