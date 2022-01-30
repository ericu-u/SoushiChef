from django.db import models
from django_mysql.models import ListTextField

# Create your models here.

class recipeModel(models.Model):
    name = models.CharField(max_length=100)
    recipe = ListTextField(
        base_field= models.CharField(max_length=1000),
        size=15,
    )
    time = models.DurationField()
    ingredients = ListTextField(
        base_field= models.CharField(max_length=125),
        size=20,
    )
    description = models.CharField(max_length=2000)
    serving_size = models.CharField(max_length=200)
    image = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name