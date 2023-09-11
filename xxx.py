from django.shortcuts import render
from .gpsapp.models import Location
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse

def geolocation(request):
    return render(request, 'gps5.html')

@csrf_protect
def guardar_ubicacion(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        
        # Verificar si se proporcionaron valores válidos para latitud y longitud
        if lat is not None and lon is not None:
            try:
                lat = float(lat)
                lon = float(lon)
                
                # Crear y guardar la ubicación en la base de datos
                location = Location(latitude=lat, longitude=lon)
                location.save()
                
                return HttpResponse('Ubicación guardada gt gt')
            except (ValueError, TypeError) as e:
                return HttpResponse(f'Error al guardar la ubicación: {str(e)}', status=400)
        else:
            return HttpResponse('Latitud y longitud faltantes en la solicitud.', status=400)
    else:
        return HttpResponse('Método no permitido', status=405)