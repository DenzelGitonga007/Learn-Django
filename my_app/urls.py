from django.urls import path
# Import views
from . import views

app_name = 'my_app'

urlpatterns = [
    path('list/', views.list, name="list_abouts"), # list all items
    path('item/<int:item_id>/details', views.read, name="item_details"), # view item details
]