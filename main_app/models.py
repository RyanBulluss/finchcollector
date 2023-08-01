from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    height = models.IntegerField()
    age = models.IntegerField()
