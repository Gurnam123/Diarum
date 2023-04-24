"""Models are defined here"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from location_field.models.plain import PlainLocationField
from mapbox_location_field.models import LocationField


class Recipe(models.Model):
    """Model Recipe for storing Recipes by users"""
    title = models.CharField(max_length=100)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True) #upload_to='images',
    memories= models.BooleanField(default= False)
    location = LocationField(map_attrs={
        "style": "mapbox://styles/mapbox/streets-v11",
        "center": [-122.4194, 37.7749],
        "zoom": 10,
        "scrollZoom": False
        })

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """function to return absolute url of the detail view of Recipe Model"""
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
