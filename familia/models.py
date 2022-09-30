from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento=models.DateField()
    edad= models.IntegerField()
    