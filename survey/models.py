
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone




class Survey(models.Model):
     name = models.CharField(max_length=45,null=True) 
     GENDER_CHOICES=(
      ("M","Male"),
       ("F","Female"),
       ("O","Other")

     )
     gender=models.CharField(max_length=20,choices=GENDER_CHOICES,null=True)
     age = models.PositiveIntegerField()
     phone_number=models.CharField(max_length=12,null=True)
     SATISFIED_CHOICES=(
      ("Y","Yes"),
      ("N","No"),

     )
     satisfied=models.CharField(max_length=5,choices=SATISFIED_CHOICES)
     feedback=models.CharField(max_length=200,null=True)
    











   






