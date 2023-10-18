from django.db import models

class Thing():
    name = models.CharField()
    desciption = models.TextField()
    quantity = models.IntegerField()