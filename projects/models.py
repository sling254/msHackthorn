from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=500,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    location = models.CharField(max_length=50,blank=True,null=True)
    picture = models.ImageField(upload_to='static/profile_pics',default='static/usericon.png',blank=True)
