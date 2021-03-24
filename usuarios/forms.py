from django import forms
from .models import Orden, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class OrdenForm(forms.ModelForm):
    class Meta:

        model = Orden
        fields = '__all__'

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
