from django.shortcuts import render, redirect
from .models import *
from .forms import OrdenForm, CrearUsuarioForm
from .filters import OrdenFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
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
    orden_filter = OrdenFilter(request.GET, queryset=ordenes)
    ordenes = orden_filter.qs

    contexto = {
        'cliente': cliente,
        'ordenes': ordenes,
        'numero_ordenes': numero_ordenes,
        'orden_filter': orden_filter
    }
    return render(request, 'clientes.html', contexto)

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        form = CrearUsuarioForm()
        if request.method == 'POST':
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cuenta Creada!!')
                return redirect('login')

        contexto = {
            'form': form
        }

        return render(request, 'registro.html', contexto)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.info(request, 'Usuario o cotrasena incorrectos!!')


        return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def actualizar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    contexto = {
        'form' : form
    }
    return render(request, 'clienteForm.html', contexto)

@login_required(login_url='login')
def eliminar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/')
    contexto = {
        'cliente': cliente
    }
    return render(request, 'eliminar_cliente.html', contexto)

@login_required(login_url='login')
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

@login_required(login_url='login')
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
@login_required(login_url='login')
def eliminar_orden(request, pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('/')
    contexto = {
        'orden': orden
    }
    return render(request, 'eliminar.html', contexto)
