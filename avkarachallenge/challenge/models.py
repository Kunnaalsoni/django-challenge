from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=64)
    tag = models.CharField(max_length=64)
    description = models.TextField()
    link = models.URLField(max_length=128)