from .serializers import VehiculoSerializer, TipoVehiculoSerializer
from rest_framework import viewsets, permissions
from .models import Vehiculo, TipoVehiculo

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehiculoSerializer

class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = TipoVehiculo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoVehiculoSerializer

