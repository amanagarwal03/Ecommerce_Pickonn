from django import forms
from django.contrib.auth.models import User
from ecommerce.models import Account , Account_aff 
from django.contrib.admin import widgets

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=('username','email','password')
# class Login_Form(forms.ModelForm):
# 	username=forms.CharField()
# 	password=forms.CharField(widget=widget=forms.PasswordInput)

class AffiliateForm(forms.ModelForm):
	class Meta:
		model =User
		fields=('username','email','first_name','last_name')
		widget = {
			'username':forms.TextInput(attrs={'class':'form-control',
				'placeholder':'ds'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
		}




class AffiliateForm2(forms.ModelForm):
	affliate_id = forms.CharField(widget=forms.HiddenInput(),initial=123)
	class Meta:
		model = Account_aff
		fields=('company','domain','title','dob','affliate_id')
		widget = {
			'company': forms.TextInput(attrs={'class':'form-control'}),
			'domain': forms.TextInput(attrs={'class':'form-control'}),
			'title' :forms.Select(attrs={'class':'form-control'}),
			'dob' :forms.DateInput(attrs={'class':'form-control'}),
			
		}