import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone 
from django.dispatch import receiver



# Create your models here.


class Neighborhood( models.Model ):

    ZONES_CHOICES=(
        ("Kisumu", "Kisumu"),
        ("Mombasa", "Mombasa"),
        ("Nairobi", "Nairobi"),
        ("Nakuru", "Nakuru"),
        ("Kilifi", "Kilifi"),
    )
    name=models.CharField( max_length=300 , null=True )
    description=models.TextField(max_length=200, null=True)
    location=models.CharField( max_length=100 , choices=ZONES_CHOICES,default="Kisumu")
    population=models.IntegerField(default=0)
    admin=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    health_contact=models.IntegerField(blank=True,null=True)
    police_contact=models.IntegerField(blank=True,null=True)
    user=models.ForeignKey( User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse( 'detail' , kwargs={'pk': self.pk} )

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def neighborhood_list(cls):
        list_of_neighborhood=cls.objects.all()
        return list_of_neighborhood

    @classmethod
    def update_neighborhood(cls,id,name):
        '''
         Method that updates user profile hoods
        '''
        return cls.objects.filter(id=id).update(hoods=name) 

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
    bio=models.CharField(max_length=20, null=True,blank=True)
    hoods=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=254, blank=True,null=True)
    contact=models.IntegerField(null=True, blank=True) 

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
    name=models.CharField(max_length=40 , null=True)
    description=models.TextField(max_length=200, null=True,blank=True)
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

class UpcomingEvents( models.Model ):
    name = models.CharField( max_length=30, null=True)
    description = models.TextField( max_length=200, null=True,blank=True)
    hood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    date = models.DateField()
    user=models.ForeignKey( User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    def save_events(self):
        self.save()

    def delete_events(self):
        self.delete()
    
    @classmethod
    def update_event(cls , id,name):
        updated_event=cls.objects.filter(id=id).update(name=name)
        return updated_event



class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post')

    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()