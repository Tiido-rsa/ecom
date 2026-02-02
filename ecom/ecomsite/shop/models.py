from django.db import models

class Product(models.Model):

    def __str__(self):
        return self.name 

    name            = models.CharField(max_length=200)
    description     = models.TextField() # TextField is used for longer text
    price           = models.DecimalField(max_digits=10, decimal_places=2) # also FloatField can be used but DecimalField is more accurate for money
    discount_price  = models.DecimalField(max_digits=10, decimal_places=2) # also FloatField can be used but DecimalField is more accurate for money
    image           = models.CharField(max_length=500)
    category        = models.CharField(max_length=200) # CharField is used for short text
    
    
