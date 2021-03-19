from django.shortcuts import render
from .models import *
# Create your views here.

def inicio(request):
    clientes = Cliente.objects.all()
    ordenes = Orden.objects.all()
    total_ordenes = ordenes.count()
    enviados = ordenes.filter(estado='enviado').count()
    pendientes = ordenes.filter(estado='pendiente').count()

    context = {
        'clientes': clientes,
        'ordenes': ordenes,
        'total_ordenes': total_ordenes,
        'enviados': enviados,
        'pendientes': pendientes
    }
    return render(request, 'dashboard.html', context)

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})