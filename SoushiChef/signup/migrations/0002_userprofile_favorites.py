# Generated by Django 3.2.5 on 2022-01-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20220129_0928'),
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(to='menu.recipeModel'),
        ),
    ]
