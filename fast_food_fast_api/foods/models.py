from django.db import models
from datetime import date

class Food(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    date_created = models.DateField(default=date.today)

class SignUp(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=6)