from django.urls import path
from . import views

urlpatterns = [
    path('geolocation/', views.geolocation, name='geolocation'),
    path('guardar_ubicacion/', views.guardar_ubicacion, name='guardar_ubicacion'),
    ]
