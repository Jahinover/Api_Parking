from django.contrib import admin
from .models import Vehiculo, TipoVehiculo

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(TipoVehiculo)
