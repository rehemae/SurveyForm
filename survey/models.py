
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     GENDER_CHOICES=(
      ("M","Male"),
       ("F","Female"),
       ("O","Other")

     )
     gender=models.CharField(max_length=20,choices=GENDER_CHOICES,null=True)
     age = models.PositiveIntegerField()
     phone_number=models.CharField(max_length=12,null=True)


     def __str__(self):
            return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.question}-{self.user}-{self.choice}"



class Feedback(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created     = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)
   
    def __str__(self):
        return self.title

class FeedbackComment(models.Model):
    forum = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.TextField()


   






