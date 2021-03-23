from django.shortcuts import render, redirect
from .models import *
from .forms import OrdenForm, ClienteForm
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

def clientes(request, pk):
    cliente = Cliente.objects.get(id=pk)
    ordenes = cliente.orden_set.all()
    numero_ordenes = ordenes.count()

    contexto = {
        'cliente': cliente,
        'ordenes': ordenes,
        'numero_ordenes': numero_ordenes
    }
    return render(request, 'clientes.html', contexto)

def crear_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    contexto = {
        'form': form
    }
    return render(request, 'clienteForm.html', contexto)

def crear_orden(request):
    form = OrdenForm()
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    contexto = {
        'form': form
    }
    return render(request, 'ordenForm.html', contexto)

def actualizar_orden(request, pk):

    orden =Orden.objects.get(id=pk)
    form = OrdenForm(instance=orden)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('/')

    contexto = {
        'form': form
    }

    return render(request, 'ordenForm.html', contexto)

def eliminar_orden(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('/')
    contexto = {
        'orden': orden
    }
    return render(request, 'eliminar.html', contexto)
