from django.db import models
from django.urls import reverse

# Create your models here.

class Exercises(models.Model):
    name = models.CharField(max_length=50) 
    muscles = models.BinaryField()              ##define muscles used as a sequence of bits 1 for yes 0 for no



# class Macrocycle(models.Model):

class Mesocycle(models.Model):
    micro = models.ForeignKey(
        'Microcycle',
        on_delete=models.CASCADE,
    )

    
class Microcycle(models.Model):
    exercise = models.CharField(max_length=50) 
    sets = models.IntegerField()
    reps = models.IntegerField()
    length = models.IntegerField()            # length of microcycle ex a week is 7
    daysOn = models.BinaryField()              #days on and off ex mon wed thur and sat
