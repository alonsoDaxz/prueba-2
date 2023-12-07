from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def reservas_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/reservas_list.html', {'reservas': reservas})

def nueva_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas_list')
    else:
        form = ReservaForm()
    return render(request, 'reservas/nueva_reserva.html', {'form': form})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/editar_reserva.html', {'form': form})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('reservas_list')

def index(request):
    datos_alumno = {
        'nombre': 'Alonso Orellana',
        'edad': 22,
        'rut': '20881491-5',
    }
    return render(request, 'index.html', {'datos_alumno': datos_alumno})





