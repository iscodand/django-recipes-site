from django.db import models
from models import Models

class Recipes(models.Models):
    recipe_name = models.CharField(max_length=30)
    
