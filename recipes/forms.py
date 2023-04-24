from . import models
from django import forms
from mapbox_location_field.widgets import MapInput

class RecipeForm(forms.ModelForm):
    location = forms.CharField(widget=MapInput(attrs={
        'mapbox_access_token': 'pk.eyJ1IjoiZ3VybmFtIiwiYSI6ImNsZ291YnJzbjBwNmgzcHFrZjY2dWRyNTgifQ.g2UGamC_vlOY6plfWpU6Rg',
        'map_style': 'mapbox://styles/mapbox/streets-v11',
        'marker_color': 'black',
        'center': '-74.50, 40',
        'zoom': 12,
        
    }))
    
    
    class Meta:
        model = models.Recipe
        fields = ['title', 'description', 'image', 'memories', 'location']