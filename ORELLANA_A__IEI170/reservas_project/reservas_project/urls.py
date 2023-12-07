"""
URL configuration for reservas_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import reservas_list, nueva_reserva, editar_reserva, eliminar_reserva, index

urlpatterns = [
    path('reservas/', reservas_list, name='reservas_list'),
    path('reservas/nueva/', nueva_reserva, name='nueva_reserva'),
    path('reservas/editar/<int:pk>/', editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:pk>/', eliminar_reserva, name='eliminar_reserva'),
    path('', index, name='index'),  
]


