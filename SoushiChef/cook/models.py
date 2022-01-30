from django.db import models

# Create your models here.
class CookEntry(models.Model):
    entry = models.CharField(max_length=100)