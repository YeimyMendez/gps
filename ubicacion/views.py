from django.shortcuts import render
from django.http import JsonResponse
from .models import Ubicacion
from .forms import UbicacionForm

def home(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'home.html', {'ubicaciones': ubicaciones})

def guardar_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Ubicación guardada con éxito'})
        else:
            return JsonResponse({'message': 'Error en la validación del formulario'})
