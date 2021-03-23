from django.db import models

# Create your models here.

class Cliente(models.Model):
    """Modelo de Usuario cliente
    """
    nombre = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    creado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """Modelo del producto en la base de datos
    """
    CATEGORIA = (
        ('categoria1', 'categoria1'),
        ('categoria2', 'categoria2'),
    )

    nombre = models.CharField(max_length=255, null=True)
    precio = models.FloatField(null=True)
    categoria = models.CharField(max_length=255, null=True, choices=CATEGORIA)
    descripcion = models.TextField(null=True)
    creado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

class Tag(models.Model):
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre
class Orden(models.Model):
    """Modelo de orden del cliente a determinado producto
    """
    ESTADOS = (
        ('pendiente', 'pendiente'),
        ('por salir', 'por salir'),
        ('enviado', 'enviado'),
    )
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=255, null=True, choices=ESTADOS)
    tags = models.ManyToManyField(Tag, null=True)

    
    def __str__(self):
        return self.producto.nombre


