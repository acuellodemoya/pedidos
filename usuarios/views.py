from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'dashboard.html')

def productos(request):
    return render(request, 'productos.html')

def clientes(request):
    return render(request, 'clientes.html')