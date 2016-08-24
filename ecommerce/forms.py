from django import forms
from django.contrib.auth.models import User
from ecommerce.models import Account

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=('username','email','password')
# class Login_Form(forms.ModelForm):
# 	username=forms.CharField()
# 	password=forms.CharField(widget=widget=forms.PasswordInput)