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
		fields=['name']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user','hoods'] 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image','email','contact'] 