from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'phone', 'location']


class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=True)



