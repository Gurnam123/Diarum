# Generated by Django 3.2 on 2023-04-20 08:04

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={'center': [-122.4194, 37.7749], 'scrollZoom': False, 'style': 'mapbox://styles/mapbox/streets-v11', 'zoom': 10}),
        ),
    ]
