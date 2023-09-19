from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guardar_ubicacion/', views.guardar_ubicacion, name='guardar_ubicacion'),
]

