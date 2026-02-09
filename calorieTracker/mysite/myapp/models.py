from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
    
    def __str__(self):
        return self.name
    
    name        = models.CharField(max_length=100)
    carbs       = models.FloatField()
    protein     = models.FloatField()
    fat         = models.FloatField()
    calories    = models.IntegerField()
    
    
class Consume(models.Model):
    
    def __str__(self):
        return self.food.name
    
    food        = models.ForeignKey(food, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)