from stockApp.models import Articulos
from django.shortcuts import render, HttpResponse
from stockApp.models import *

"""
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    contacto = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=30)

"""

def agregarCliente(request):  
    catchNombre = request.GET ["add_name"]
    catch_parentezco = request.GET ["add_paren"]
    if len(catchNombre) != 0:
        clienteNuevo = Cliente.objects.create(nombre = catchNombre,parentezco = catch_parentezco)
        return mostrarTodos(request)
    else:
        mensaje = "Debe ingresar un valor"
        return HttpResponse(mensaje)

def mostrarTodos(request):
    todos = Cliente.objects.all()
    return render(request,"home.html", {"clientes":todos})
    