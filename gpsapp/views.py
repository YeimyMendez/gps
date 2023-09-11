from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from django.views.decorators.csrf import csrf_protect


def geolocation(request):
    return render(request, 'gps3.html')


@csrf_protect
def guardar_ubicacion(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        location = Location(latitude=lat, longitude=lon)
        try:
            location.save()
            print("==========")
            return HttpResponse('Ubicación guardada GT')
            print("==========")
        except Exception as e:
            # Cambiado a status=400 en caso de error
            return HttpResponse(f'Error al guardar la ubicación: {str(e)}', status=400)
    else:
        return HttpResponse('Método no permitido', status=405)
