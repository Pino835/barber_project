from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    service = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Cita de {self.client.username} para {self.service} el {self.date}'
