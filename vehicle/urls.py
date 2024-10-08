from django.urls import path
from . import views

urls = [
    path('', views.vehicle_list, name='Vehicle_names'),
    path('add/', views.add_vehicle, name='Add_vehicle'),
]
