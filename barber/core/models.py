from django.db import models
from django.contrib.auth.models import User

class Cita(models.Model):
    
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )

    def __str__(self):
        return f"Cita de {self.cliente.username} el {self.fecha} a las {self.hora}"


