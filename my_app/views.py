from django.shortcuts import render
# Import views
from .models import About
# Create your views here.

""" CRUD functionality
    C - Create
    R - Read
    U - Update
    D - Delete
"""

# Read
def read(request):
    # Get all abouts in the db
    abouts = About.objects.all()
    context = { 'abouts': abouts } # Map each about to a key, as a key-value pair dictionary
    return render(request, 'my_app/list_abouts.html', context)

