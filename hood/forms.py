from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Business,Neighborhood,Profile,UpcomingEvents,Post



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class BusinessForm(forms.ModelForm):

	class Meta:
		model=Business
		fields=['name', 'description','image','business_email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user','bio','hoods'] 

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields=['image', 'bio','email'] 

class NeighborhoodForm(forms.ModelForm):

	class Meta:

		model=Neighborhood
		fields=['name' ,'image', 'description' , 'location' ,'admin', 'population','health_contact','police_contact'] 


class EventsForm(forms.ModelForm):

	class Meta:

		model=UpcomingEvents
		fields=['name','description','date']


class PostForm(forms.ModelForm):

	class Meta:

		model=Post
		fields=['title','post'] 

