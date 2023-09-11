# En celery.py
from __future__ import absolute_import, unicode_literals
import os
from urllib import request
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gps.settings')
app = Celery('gps')

# Configuración de Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Tarea programada para guardar ubicación cada minuto
@app.task
def guardar_ubicacion_periodicamente():
    from xxx import guardar_ubicacion
    response = guardar_ubicacion(request)  # Aquí debes crear un objeto request válido

    # Puedes verificar la respuesta para asegurarte de que se guardó correctamente
    if response.status_code == 200:
        print('Ubicación guardada correctamente.')
    else:
        print('Error al guardar la ubicación.')
