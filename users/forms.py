"""Forms for user registeration"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Class-based registeration form"""
    email = forms.EmailField()

    class Meta:
        """Meta class to dictated which fields are required"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
