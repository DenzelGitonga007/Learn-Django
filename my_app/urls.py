from django.urls import path
# Import views
from . import views

app_name = 'my_app'

urlpatterns = [
    path('list/', views.read, name="list_abouts")
]