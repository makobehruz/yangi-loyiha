from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

