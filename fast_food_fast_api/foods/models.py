from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
