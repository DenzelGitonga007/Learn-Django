from django.shortcuts import render, get_object_or_404
# Import views
from .models import About
# Create your views here.

""" CRUD functionality
    C - Create
    R - Read
    U - Update
    D - Delete
"""

# List
def list(request):
    # Get all abouts in the db
    abouts = About.objects.all()
    context = { 'abouts': abouts } # Map each about to a key, as a key-value pair dictionary
    return render(request, 'my_app/list_abouts.html', context)

# Read
def read(request, item_id):
    item = get_object_or_404(About, pk=item_id) # get the item by id
    context = { 'item': item }
    return render(request, 'my_app/item_details.html', context)
