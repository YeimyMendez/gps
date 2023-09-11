from django.contrib import admin
from .models import Location  # Importa el modelo que deseas administrar

# Define una clase de administración para el modelo Location
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude')  # Campos a mostrar en la lista
    search_fields = ('latitude', 'longitude')  # Campos de búsqueda

