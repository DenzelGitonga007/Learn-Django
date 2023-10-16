from django.shortcuts import render, get_object_or_404, redirect
# Import views
from .models import About
# Import the form(s)
from .forms import CreateAboutForm
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
    about = get_object_or_404(About, pk=item_id) # get the item by id
    context = { 'about': about }
    return render(request, 'my_app/about_details.html', context)

# Create
def create(request):
    if request.method == 'POST':
        form = CreateAboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:list_abouts')
    else:
        form = CreateAboutForm()
    context = {
        'form': form
    }
    return render(request, 'my_app/create_about.html', context)