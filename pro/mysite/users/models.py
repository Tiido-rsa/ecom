from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #establishing a one-to-one relationship between the User and Profile models
    image = models.ImageField(default='man_706826.png', upload_to='profile_pics')
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

        