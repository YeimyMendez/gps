from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Search, Location
from .forms import SearchForm
from .geoip import obtener_informacion_de_ubicacion
import folium
import geocoder

# Create your views here.

def geolocation(request):
    return render(request, 'gps.html')

# @csrf_protect
# def guardar_ubicacion(request):
#     if request.method == 'POST':
#         lat = request.POST.get('lat')
#         lon = request.POST.get('lon')
#         location = Location(latitude=lat, longitude=lon)
#         try:
#             location.save()
#             # Redireccionar a la página 'gps.html' una vez que se haya guardado la ubicación
#             return redirect('geolocation')
#         except Exception as e:
#             # Cambiado a status=400 en caso de error
#             return HttpResponse(f'Error al guardar la ubicación: {str(e)}', status=400)
#     else:
#         return HttpResponse('Método no permitido', status=405)


def obtener_ip_cliente(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_cliente = x_forwarded_for.split(',')[0]
    else:
        ip_cliente = request.META.get('REMOTE_ADDR')
    return ip_cliente

@csrf_protect
def guardar_ubicacion(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        
        # Utiliza la función para obtener información de ubicación basada en la dirección IP del cliente
        user_ip = request.META['REMOTE_ADDR']
        ubicacion = obtener_informacion_de_ubicacion(user_ip)
        
        if ubicacion:
            # Puedes acceder a los datos de ubicación desde 'ubicacion' y utilizarlos en tu aplicación
            # Por ejemplo: ubicacion['country_name'], ubicacion['region'], ubicacion['city'], etc.
            
            location = Location(latitude=lat, longitude=lon, ip_address=user_ip, ubicacion=ubicacion)
            try:
                location.save()
                # Redireccionar a la página 'gps.html' una vez que se haya guardado la ubicación
                return redirect('geolocation')
            except Exception as e:
                # Manejado en caso de error al guardar la ubicación
                return HttpResponse(f'Error al guardar la ubicación: {str(e)}', status=400)
        else:
            # Maneja el caso en el que no se pueda obtener la información de ubicación
            return HttpResponse('No se pudo obtener la información de ubicación', status=400)
    else:
        return HttpResponse('Método no permitido', status=405)

    
@csrf_protect
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            form.save()
        else:
            # Manejar el caso en que el formulario no sea válido (puedes agregar código adicional aquí)
            address = None
    else:
        form = SearchForm()
        address = None
    
    if address:
        location = geocoder.osm(address)
        if location.latlng:
            lat, lng = location.latlng
            country = location.country
            # Crear Map Object
            m = folium.Map(location=[lat, lng], zoom_start=8)
            folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
            # Obtener HTML Representation del objeto Map
            m = m._repr_html_()
        else:
            return HttpResponse('La dirección proporcionada es inválida', status=400)
    else:
        m = None
    
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)



