from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

    #get_absolute_url sets a url -> currently targeting self
    #reverse is like url template tag, can 
    #pass in name field to specificy url

    #kwargs is not required but is needed for the detail page 
    #because it contains the id for each details page