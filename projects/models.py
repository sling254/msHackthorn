from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=500,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    location = models.CharField(max_length=50,blank=True,null=True)
    picture = CloudinaryField('image',default='static/usericon.png',blank=True)

    def __str__(self):
        return f"{self.user.name}'s Profile"

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    image = CloudinaryField('images',blank=True)
    live_link = models.CharField(max_length=50,blank=True,null=True)
    github_like = models.CharField(max_length=50,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Project"
