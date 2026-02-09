from django.db import models

class Link(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else self.url