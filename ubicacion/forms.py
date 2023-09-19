from django import forms
from .models import Ubicacion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ('latitud', 'longitud')
