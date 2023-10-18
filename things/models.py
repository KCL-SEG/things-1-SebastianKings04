from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator



class Thing():
    name = models.CharField(unique=True, blank=False,max_length=30)
    desciption = models.TextField(unique=False,blank=True, max_length=120)
    quantity = models.IntegerField(unique = False, validators=[MaxValueValidator(100), MinValueValidator(0)])