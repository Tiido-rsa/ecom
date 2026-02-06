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
    
    
class Order(models.Model):
    
    def __str__(self):
        return self.name + ' - ' + self.email
    
    items       = models.CharField(max_length=1000) 
    # This will store the items in the order as a string (e.g., "item1, item2, item3")
    
    name        = models.CharField(max_length=200)
    email       = models.EmailField()
    address     = models.CharField(max_length=300)
    suburb      = models.CharField(max_length=100, default='')  # Added suburb field
    province    = models.CharField(max_length=100)
    city        = models.CharField(max_length=100)
    zip_code    = models.CharField(max_length=20)
    total       = models.CharField(max_length=20, default='1')


class Wishlist(models.Model):
    
    def __str__(self):
        return self.name + ' - ' + self.email
    
    items       = models.CharField(max_length=1000) 
    # This will store the items in the wishlist as a string (e.g., "item1, item2, item3")
    
    name        = models.CharField(max_length=200)
    email       = models.EmailField()