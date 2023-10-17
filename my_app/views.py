from django.shortcuts import render, get_object_or_404, redirect
# Import views
from .models import About
# Import the form(s)
from .forms import CreateAboutForm, UpdateAboutForm
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

# Read
def read(request, about_id):
    about = get_object_or_404(About, pk=about_id) # get the about by id
    context = { 'about': about }
    return render(request, 'my_app/about_details.html', context)

# Update
def update(request, about_id):
    about = get_object_or_404(About, pk=about_id) # get the about by the id
    if request.method == 'POST':
        form = UpdateAboutForm(request.POST, instance=about) # refer the about instance
        if form.is_valid():
            form.save()
            return redirect('my_app:about_details', about_id)
    else:
        form = UpdateAboutForm(instance=about)
    context = {
        'form': form
        }
    return render(request, 'my_app/update_about.html', context)


# Continue from here