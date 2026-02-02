from django.db import models

class Moviedata(models.Model):
    name        = models.CharField(max_length=100)
    rating      = models.FloatField()
    year        = models.IntegerField()
    typ         = models.CharField(max_length=200, default='Action')
    image       = models.ImageField(upload_to='images', default='images/default.avif')
    duration    = models.FloatField()
    genre       = models.CharField(max_length=200, default='Action')
    
    def __str__(self):
        return self.name    