from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']