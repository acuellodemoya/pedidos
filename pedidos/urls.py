"""pedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import inicio, productos, clientes, crear_orden, actualizar_orden, eliminar_orden, crear_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('clientes/<str:pk>/', clientes, name='clientes'),
    path('crear_orden/', crear_orden, name='crear_orden'),
    path('actualizar_orden/<str:pk>', actualizar_orden, name='actualizar_orden'),
    path('eliminar_orden/<str:pk>', eliminar_orden, name='eliminar_orden'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
]
