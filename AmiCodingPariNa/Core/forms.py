from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Payload
class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"password1",'id':"name"}))
    password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput(attrs={"class":"password1",'id':"name"}))
    class Meta:
        
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'uname','id':"name",'placeholder':"Enter Your Username"}),
            'first_name':forms.TextInput(attrs={'class':'fname','id':'name','placeholder':'Enter Your First Name'}),
            'last_name':forms.TextInput(attrs={'class':'fname','id':'name','placeholder':'Enter Your Last Name'}),
            'email':forms.EmailInput(attrs={'class':'email','id':'name','placeholder':'example: kawsar@gmail.com'}),
            'password1':forms.PasswordInput (attrs={'class':'password','id':'name'}),
        }



class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'uname','id':"name",'placeholder':"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'password','id':"name",'placeholder':"Password"}))
    model=User

class KhojTheSearchForm(forms.ModelForm):
    search_value=forms.IntegerField(label="Search Values",widget=forms.NumberInput(attrs={'class':'search','id':'name'}) )
    class Meta:
        model=Payload
        fields=["input_value"]
        labels={'input_value':"Input Values"}
        widgets={
            'input_value':forms.TextInput(attrs={'class':'uname','id':"name",'placeholder':"number list"}),
            }

        
