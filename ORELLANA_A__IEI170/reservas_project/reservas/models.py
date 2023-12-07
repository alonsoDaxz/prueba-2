from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Reserva(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo_electronico = models.EmailField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_reserva}"

from django.db import models

class Reserva(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo_electronico = models.EmailField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_reserva}"
