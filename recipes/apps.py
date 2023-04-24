"""apps.py -- configuring our application here to register with django"""
from django.apps import AppConfig


class RecipesConfig(AppConfig):
    """class RecipeConfig to create configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
