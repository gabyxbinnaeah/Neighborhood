# Generated by Django 3.1.7 on 2021-07-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0013_neighborhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
