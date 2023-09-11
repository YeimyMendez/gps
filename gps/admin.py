from django.contrib import admin
from gpsapp.models import Location  # Importa el modelo

# Registra la aplicación y el modelo en el panel de administración
admin.site.register(Location)
