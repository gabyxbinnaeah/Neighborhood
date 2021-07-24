from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Business,Neighborhood,Profile



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
        fields=['image', 'bio','email','contact'] 

class NeighborhoodForm(forms.ModelForm):

	class Meta:

		model=Neighborhood
		fields=['name' , 'description' , 'location' , 'population','hood','health_contact','police_contact'] 

