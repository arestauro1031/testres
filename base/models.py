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
    
    def __str__(self):
        #return str(self.name) when returning an str wrapped it with str(value)
        return self.name
    
class Message(models.Model):
    #user = 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        #return str(self.name) when returning an str wrapped it with str(value)
        return self.body[0:50] #note: trim it down to 50 characters
    
class Employees(models.Model):
    emp_name = models.CharField (max_length=50, null=False, blank=False)
    hourly_pay = models.DecimalField(max_digits=5, decimal_places=2)
    join_date = models.DateField(null=True, blank=True)