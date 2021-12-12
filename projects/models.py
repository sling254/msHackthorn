from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import datetime as dt
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile', on_delete=models.CASCADE)
    username = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=500,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    location = models.CharField(max_length=50,blank=True,null=True)
    picture = CloudinaryField('image',default='static/usericon.png',blank=True)
    email = models.EmailField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    
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
    github_link = models.CharField(max_length=50,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    @classmethod
    def search_projects(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    def __str__(self):
        return f"{self.user.username}'s Project"


class Rate(models.Model):
  content_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  content_wise_average = models.FloatField(default=0.0,blank=True)
  usability_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  usability_wise_average = models.FloatField(default=0.0,blank=True)
  design_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  design_wise_average = models.FloatField(default=0.0,blank=True)
  aggregate_average_rate = models.FloatField(default=0.0,blank=True)
  project = models.ForeignKey(Project,on_delete=CASCADE)
  user = models.ForeignKey(User,on_delete=CASCADE)


  def save_rating(self):
      self.save()

  @classmethod
  def get_ratings(cls, id):
      ratings = Rate.objects.filter(project_id=id).all()
      return ratings

  def __str__(self):
      return f'{self.project} Rating'
