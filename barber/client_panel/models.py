from django.db import models
from django.contrib.auth.models import User
from admin_panel.models import Service

# Create your models here.

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_app')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_app')
    date = models.DateTimeField()

    def __str__(self):
        return f'Cita de {self.client.username} para {self.service} el {self.date}'
