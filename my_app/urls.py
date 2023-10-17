from django.urls import path
# Import views
from . import views

app_name = 'my_app'

urlpatterns = [
    path('list/', views.list, name="list_abouts"), # list all items
    path('about/<int:about_id>/details', views.read, name="about_details"), # view item details
    path('about/create', views.create, name="create_about"), # create the about
    path('update/<int:about_id>/details', views.update, name="update_about"), # update about
]