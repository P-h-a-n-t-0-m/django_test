from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class FormUser(UserCreationForm):
    my_images = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "my_images"]


class UpdateProfile(UserChangeForm):
    my_images = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "email", "my_images"]
