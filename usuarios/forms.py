from django import forms
from .models import Orden, Cliente


class OrdenForm(forms.ModelForm):
    class Meta:

        model = Orden
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:

        model = Cliente
        fields = ['nombre', 'telefono', 'email']