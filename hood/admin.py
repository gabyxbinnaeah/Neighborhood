from django.contrib import admin
from .models import Neighborhood,Profile,Business,UpcomingEvents


# Registers models.

admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(UpcomingEvents)