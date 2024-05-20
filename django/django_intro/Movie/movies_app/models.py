from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    url_Image = models.TextField()
    duration = models.IntegerField()


class Actor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    actor_in_movie = models.ManyToManyField(Movie, related_name='act')

class Category(models.Model):
    categoryGenre = models.CharField(max_length=45)
    movieCategory = models.ManyToManyField(Movie, related_name='genre')
