from django.contrib import admin
from .models import ClientProfile, Appointment

# Register your models here.

admin.site.register(ClientProfile)
admin.site.register(Appointment)
