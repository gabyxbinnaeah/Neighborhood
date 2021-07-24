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
    hoods=models.TextFields(max_length=100)
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


class Neighbourhood( models.Model ):
    name=models.CharField( max_length=300 , null=True )
    description=models.CharField(max_length=500 , null=True)
    location=models.CharField( max_length=100 , choices=CITY_CHOICES )
    population=models.IntegerField(default=0)
    user=models.ForeignKey( User, on_delete=models.CASCADE )
    hoods=(
        ('Nairobi' , 'Nairobi'),
        ('Kisumu' , 'Kisumu'),
        ('Mombasa' , 'Mombasa'),
        ('Malindi' , 'Malindi'),
        ('Nakuru','Nakuru'),
    )

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )

    def save_hood(self):
        self.save( )

    def delete_hood(self):
        self.delete( )

    @classmethod
    def update_neighborhood(cls,id,hoods):
        '''
         Method that updates user profile hoods
        '''
        return cls.objects.filter(id=id).update(hoods=hoods) 

    @classmethod
    def search_hood(cls , search_term):
        hoods=cls.objects.filter( name__icontains=search_term )
        return hoods

    def __str__(self):
        return self.name    