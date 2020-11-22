from stockApp.models import Articulos
from django.shortcuts import render, HttpResponse
from stockApp.models import *

def agregarCliente(request):  
    if request.GET ["add"]:
        catchNombre = request.GET ["add"]
        clienteNuevo = Cliente.objects.create(nombre = catchNombre)
        return mostrarTodos(request)
    else:
        mensaje = "Debe ingresar un valor"
    
    return HttpResponse(mensaje)

def mostrarTodos(request):
    todos = Cliente.objects.all()
    return render(request,"home.html", {"clientes":todos})
    