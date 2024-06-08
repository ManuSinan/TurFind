from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LoginUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)

    class Meta:
        model = LoginUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class TurfOwnerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)

    class Meta:
        model = LoginUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']
