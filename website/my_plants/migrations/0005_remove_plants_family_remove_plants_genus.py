# Generated by Django 5.1.4 on 2025-01-14 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_plants', '0004_remove_plants_light_remove_plants_soil_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='family',
        ),
        migrations.RemoveField(
            model_name='plants',
            name='genus',
        ),
    ]
