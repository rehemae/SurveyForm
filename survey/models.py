
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
     first_name = models.CharField(max_length=12,null=True) 
     GENDER_CHOICES=(
      ("M","Male"),
       ("F","Female"),
       ("O","Other")

     )
     gender=models.CharField(max_length=20,choices=GENDER_CHOICES,null=True)
     age = models.PositiveIntegerField()
     phone_number=models.CharField(max_length=12,null=True)


     def __str__(self):
            return str(self.first_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.first_name()




class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question





class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    CHOICE_CHOICES=(
      ("Y","Yes"),
      ("N","No"),

     )
    choice=models.CharField(max_length=5,choices=CHOICE_CHOICES)
    
    def __str__(self):
        return f"{self.question}-{self.question}-{self.choice}"



class Feedback(models.Model):
    text = models.TextField(max_length=200,blank=False,null=False)

    class Meta:
        ordering = ('text',)
   
    def __str__(self):
        return self.text


   






