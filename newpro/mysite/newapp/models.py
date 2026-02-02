from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.FloatField()
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name