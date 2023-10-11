from django.contrib import admin
# Import models
from .models import About
# Register your models here.
# Customize the admin view
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
admin.site.register(About, AboutAdmin)
