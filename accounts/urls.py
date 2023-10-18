from django.urls import path
# from django.contrib.auth import views as auth_views # Import the default user auth
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name="login"), # login
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"), # logout

    path('login/', views.CustomLoginView.as_view(), name="login"), # custom login
    path('register/', views.register, name="register"), # register
]