from django.shortcuts import render, redirect
from .models import Vehicle
from .Forms import VehicleForm

def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle/add_vehicle.html', {'form': form})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle/vehicle_list.html', {'vehicles': vehicles})
 


