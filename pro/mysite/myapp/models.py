from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManger
from django.utils import timezone

## Item Model
class Item(models.Model):

    class Meta:
        indexes =[
            models.Index(fields = ['user_name', 'item_price']),
        ]

    def __str__(self):
        return self.item_name + " : " + str(self.item_price)

    def get_absolute_url(self):
        return reverse("myapp:index")
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


    user_name           = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name           = models.CharField(max_length=200, db_index=True)
    item_price          = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    item_description    = models.CharField()
    item_image          = models.URLField(max_length=500, default='https://cdn-icons-png.freepik.com/512/7997/7997145.png')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    is_available        = models.BooleanField(default=True)

    #SOFT-DELETE
    is_deleted          = models.BooleanField(default=False) # soft-delete flag
    deleted_at          = models.DateTimeField(null=True, blank=True) # soft-delete timestamp

    objects             = ItemManger()
    all_objects         = models.Manager()
## End Item Model

## Category Model
class Category(models.Model):

    def __str__(self):
        return self.name

    name                = models.CharField(max_length=200)
    description         = models.CharField()
    image               = models.URLField(max_length=500, default='https://cdn-icons-png.freepik.com/512/7997/7997145.png')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
## End Category Model   

 