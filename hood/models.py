import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone 
from django.dispatch import receiver



# Create your models here.


class Neighborhood( models.Model ):
    name=models.CharField( max_length=300 , null=True )
    description=models.CharField(max_length=500 , null=True)
    location=models.CharField( max_length=100 , null=True)
    population=models.IntegerField(default=0)
    health_contact=models.IntegerField(blank=True,null=True)
    police_contact=models.IntegerField(blank=True,null=True)
    user=models.ForeignKey( User, on_delete=models.CASCADE )

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

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

class Profile(models.Model):
    '''
    model that defines user profile.
    '''
    image=CloudinaryField('image',blank=True,null=True)
    hoods=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
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
  


class Business( models.Model ):
    name=models.CharField( max_length=40 , null=True )
    image=CloudinaryField('image',blank=True,null=True)
    user=models.ForeignKey( User , on_delete=models.CASCADE , null=True , related_name="business" )
    hood=models.ForeignKey( Neighborhood, on_delete=models.CASCADE)
    business_email=models.EmailField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )


    def save_business(self):
        self.save( )

    @classmethod
    def delete_business_by_id(cls , id):
        businesses=cls.objects.filter( pk=id )
        businesses.delete()

    @classmethod
    def get_businesses_by_id(cls , id):
        searched_business=cls.objects.get( pk=id )
        return searched_business

    @classmethod
    def filter_business_by_location(cls , location):
        business_in_neighborhood=cls.objects.filter( location=location )
        return business_in_neighborhood

    @classmethod
    def search_businesses(cls , search_term):
        found_business=cls.objects.filter( business_name__icontains=search_term )
        return found_business

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses 

class user_hood( models.Model ):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    hood_id=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

