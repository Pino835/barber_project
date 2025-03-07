from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services_admin')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
