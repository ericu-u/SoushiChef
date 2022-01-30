from django.db import models
from menu.models import recipeModel

# Create your models here.

class userprofile(models.Model):
    # User Information
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    favorites = models.ManyToManyField(recipeModel)

    def __str__(self):
        return self.username