from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

# Registration
from . forms import RegistrationForm
from django.contrib.auth import login

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/registration/login.html' # the dir for the templates
    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_app:list_abouts')
    else:
        form = RegistrationForm
    context = {
        'form': form
        }
    return render(request, 'accounts/registration/register.html', context)