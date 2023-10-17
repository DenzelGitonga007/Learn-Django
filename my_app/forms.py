from django import forms
from .models import About

# Form to create about
class CreateAboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


# Form to update about
class UpdateAboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'