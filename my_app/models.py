from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(null=True)

    """ Stingify the fields name """
    def __str__(self):
        return self.name

