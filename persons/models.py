from django.db import models

class Person(models.Model):
    person_name = models.CharField(max_length=100) 
    person_email = models.CharField(max_length=100)
