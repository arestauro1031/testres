from django.db import models

# Create your models here.

#note: comment out columns that are useful for later
#note: the difference between now_add and auto_now is that data from now_add cannot be change after it was added while the auto_now will change everytime it is updated
class Room(models.Model):
    #host=
    #topic=
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants=
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)  