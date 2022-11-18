from rest_framework import serializers
from .models import Vehiculo, TipoVehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Vehiculo
        fields = ('vehiculo_id', 'placa', 'propietario', 'tipoVehiculo', 'empresa', 'created')

class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta():
        model = TipoVehiculo
        fields = ('tipo_id', 'nombre')