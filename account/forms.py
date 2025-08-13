from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name','username','email','password')

class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = CustomUser
        fields = ('email','username','password')

