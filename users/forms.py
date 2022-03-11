from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username',max_length=128, widget=forms.TextInput)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class EditUserProfileForm(forms.Form):
    username = forms.CharField(max_length=128)
    bio = forms.CharField(widget=forms.Textarea())
    pic = forms.ImageField(required=False)
