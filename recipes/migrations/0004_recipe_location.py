# Generated by Django 3.2 on 2023-04-20 07:35

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_memories'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='POINT(-74.0060 40.7128)', max_length=63),
        ),
    ]
