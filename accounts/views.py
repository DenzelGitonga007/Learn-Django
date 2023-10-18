from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/registration/login.html' # the dir for the templates
    
