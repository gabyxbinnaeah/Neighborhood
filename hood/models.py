import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone 
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    '''
    model that defines user profile.
    '''
    image=CloudinaryField('image',blank=True,null=True)
    bio=models.TextFields(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=254, blank=True,null=True)
    contact=models.TextField(max_length=40,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 
    @classmethod 
    def get_profile(cls):
       profile=Profile.objects.all()
       return profile 

    @classmethod
    def search_profile(cls):
        found_profile=cls.objects.filter(user__username__icontains=search_term)
        return found_profile 
        