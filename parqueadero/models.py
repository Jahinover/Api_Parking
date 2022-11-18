#from tabnanny import verbose
from django.db import models

# Create your models here.

class TipoVehiculo(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Tipo de vehiculo"
        verbose_name_plural = "Tipos de Vehiculo"
    
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    vehiculo_id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=6)
    propietario = models.CharField(max_length=100)
    tipoVehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["placa"]
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
    
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.vehiculo_id, self.placa, self.propietario, self.tipoVehiculo, self.empresa)