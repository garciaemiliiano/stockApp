from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from clientes.models import *


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
    return render(request,"clientes_templates/clientes.html", {"clientes":todos})
    