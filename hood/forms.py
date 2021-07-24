from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Business,Neighborhood



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class BusinessForm(forms.ModelForm):
	class Meta:
		model=Business
		fields=['name']