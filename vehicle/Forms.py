from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class main:
        model = Vehicle
        fields = ['model', 'year',]
