from django.db import models

class Thing():
    name = models.CharField(blank=False)
    desciption = models.TextField(unique = False)
    quantity = models.IntegerField()