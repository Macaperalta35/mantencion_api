# Commit 2: Modelos ORM implementados para TI3041

from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Equipo(models.Model):
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="equipments")
    name = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=100, unique=True)
    critical = models.BooleanField(default=False)
    installed_at = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class Tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    specialty = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class PlanMantencion(models.Model):
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="plans")
    name = models.CharField(max_length=150)
    frequency_days = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OrdenTrabajo(models.Model):
    STATUS_CHOICES = [
        ("pendiente", "Pendiente"),
        ("progreso", "En Progreso"),
        ("completado", "Completado"),
    ]

    plan = models.ForeignKey(PlanMantencion, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    technician = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendiente")
    scheduled_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"OT #{self.id} - {self.status}"


# Create your models here.
