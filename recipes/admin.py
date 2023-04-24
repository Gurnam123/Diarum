"""admin.py to register our model with the admin class -- to have django's inbuilt admin panel"""
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Recipe)
