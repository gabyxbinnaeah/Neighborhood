# Generated by Django 3.1.7 on 2021-07-25 09:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0012_remove_neighborhood_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
