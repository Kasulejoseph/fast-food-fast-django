from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator


class SignUp(models.Model):
    username = models.CharField(max_length=30, validators=[MinLengthValidator(5)])
    email = models.EmailField(max_length=100) 
    password = models.CharField(max_length=6)

class Food(models.Model):
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE )
    dish = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.IntegerField()
    date_created = models.DateField(default=date.today)

    def __str__(self):
        return str(self.user.username)
